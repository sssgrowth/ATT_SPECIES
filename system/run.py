# coding=utf-8
import argparse
from dao.load_data import *
import torch
import time

v=9
torch.manual_seed(v)

parser=argparse.ArgumentParser(description='some params')
parser.add_argument('-m','--run_mode',default='train', help='train/test/tune')
parser.add_argument('--model_name',default=None, help='the model name you use')
parser.add_argument('-mp','--model_path',default='path', help='load model in this path')
parser.add_argument('--split_train_file',type=int,default=0, help='0/1')
parser.add_argument('-s','--split_parts',type=int,default=10, help='how many pieces that one epoch split into')
parser.add_argument('--save_steps',type=int,default=1000, help='how many steps to save a model')
parser.add_argument('-t','--task',default='SemiEval2018', help='NYT SemiEval2018')
parser.add_argument('--class_config',default=None, help='the class file')
parser.add_argument('-tf','--train_file',default=None, help='one training file')
parser.add_argument('-tdp','--train_data_dir',default=None, help='path of training data directory')
parser.add_argument('-fsf','--test_file',default=None, help='one test file')
parser.add_argument('-tsdp','--test_data_dir',default=None, help='directory of test file')
parser.add_argument('-ub','--use_bert',type=int, default=0, help='0/1')
parser.add_argument('-bed','--bert_dir',default=None, help='directory loading bert model')
parser.add_argument('-sm','--save_model_dir',default=None, help='save model to directory')
parser.add_argument('-tl','--test_log',default=None, help='test results log')
parser.add_argument('--feature_based',type=int, default=0, help='use feature_based or not')
# parser.add_argument('--test_log',default=None, help='path to save the test results')
parser.add_argument('--max_sentence_length',type=int, default=512, help='sequence length')
parser.add_argument('--epoch',type=int, default=100, help='sequence length')
parser.add_argument('--class_num',type=int, default=23, help='23')
parser.add_argument('--lr',type=float, default=1e-5, help='1e-5')
parser.add_argument('--use_word_embeding',type=int,default=0, help='0/1')
parser.add_argument('--word_embeding_path',default=None, help='word embedding hdf5 file')
parser.add_argument('--vocab_path',default=None, help='vocab path pkl')
parser.add_argument('--build_vocab',default=None, help='build vocab path pkl')
parser.add_argument('--use_char_embed',type=int, default=0, help='whether to use char embeding')
parser.add_argument('--charcab_path',default=None, help='charcab file')
parser.add_argument('--output_result',default=None, help='output the prediction reulst')
parser.add_argument('--step',default=0, type=int, help='output the prediction reulst')
parser.add_argument('--class_list',default=None, help='output the prediction reulst')
parser.add_argument('--show_attention',default=0, type=int, help='output the prediction reulst')
parser.add_argument('--attention_file',default=None, help='output the prediction reulst')

args = parser.parse_args()
load_data=Load_data(args)
args.class_num=load_data.class_num
args.class_list=load_data.class_list

if args.model_name=='BERT_Base':
	from model.BERT_Base import *
	model=BERT_Base(args)

if args.model_name=='H_LSTM':
	from model.H_LSTM import *
	model=H_LSTM(args)

if args.model_name=='H_CNN':
	from model.H_CNN import *
	model=H_CNN(args)

if args.model_name=='H_LSTM_ATT':
	from model.H_LSTM_ATT import *
	model=H_LSTM_ATT(args)

if args.model_name=='H_LSTM_ATT_ext':
	from model.H_LSTM_ATT_ext import *
	model=H_LSTM_ATT_ext(args)

if args.model_name=='Gen':
	from model.Gen import *
	model=Gen(args)

if args.model_name=='Gen_GE':
	from model.Gen_GE import *
	model=Gen_GE(args)

if args.model_name=='CNN':
	from model.CNN import *
	model=CNN(args)

if args.model_name=='LSTM':
	from model.LSTM import *
	model=LSTM(args)

if args.model_name=='H_MLP_ATT':
	from model.H_MLP_ATT import *
	model=H_MLP_ATT(args)


if args.run_mode in ['test','tune']:
	print ('load model----------',args.model_path)
	# self.load_state_dict(torch.load(restore))
	pretrained_dict=torch.load(args.model_path)
	model_dict=model.state_dict()
	pretrained_dict={k:v for k,v in pretrained_dict.items() if k in model_dict}
	model_dict.update(pretrained_dict)
	model.load_state_dict(model_dict)

model=model.cuda()

c=0
prediction_result=[]
test_label=[]

t=time.time()

scheduler = torch.optim.lr_scheduler.StepLR(model.optimizer, step_size=1, gamma=0.9, last_epoch=-1)
for i in range(args.epoch):

	# lr=args.lr*0.9**i
	# # update learning rate
	# for g in model.optimizer.param_groups:
	# 	g['lr'] = lr
	#scheduler.step()
	print('learning rate',model.optimizer)

	if args.run_mode in ['train','tune']:
		f=open(args.train_file,'rb')
	if args.run_mode == 'test':
		f=open(args.test_file,'rb')

	non_line=0
	while True:
		# if c>300:
		# 	break
		t1=time.time()
		s=f.readline().decode('utf8')
		s=s.strip()
		if non_line>10:
			break
		if s=='':
			non_line+=1
			print("None line")
			continue
		if s is None:
			break
		
		non_line=0
		c+=1
		args.step=c
		if args.run_mode=='train':
			instance=load_data.convert_pubmed(s)
			model.optimizer.zero_grad()
			model(instance)
			loss=model.loss
			loss.backward()
			model.optimizer.step()
			t2=time.time()

			sys.stdout.write('\rtrain:{:10d} loss:{:.6f} batch time: {:.2f}s to time:{:8.2f}h\n'.format(
				c
				,loss
				,t2-t1
				,(t2-t)/3600.0)
			)
			sys.stdout.flush()

			if c%args.save_steps==0 and c>1:
				model_path='{}/model-{}.pt'.format(args.save_model_dir,c)
				print('-----saving model---')
				torch.save(model.state_dict(),model_path)

		if args.run_mode=="test":
			# print(s)
			model.eval()
			instance=load_data.convert_pubmed(s)
			test_label.append(instance['label'])
			model.build(instance)
			logit=model.prediction
			# because I didn't use sigmoid
			if args.model_name!='Gen':
				logit=torch.sigmoid(logit)
			pred=logit.cpu().detach().numpy()
			prediction_result.append(pred[0])

			t2=time.time()
			sys.stdout.write('\rtest:{:10d} batch time: {:.2f}s to time:{:8.2f}h\n'.format(
				c
				,t2-t1
				,(t2-t)/3600.0)
			)
			sys.stdout.flush()

	f.close()

if args.run_mode=="test":
	assert(len(prediction_result)==len(test_label))
	load_data.eval_data(prediction_result,test_label)


