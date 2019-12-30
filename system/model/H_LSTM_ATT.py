import os
import sys
sys.path.append('..')
import torch
from model.Base_Model import *

class H_LSTM_ATT(Base_Model):
	def __init__(self,args):
		super(H_LSTM_ATT,self).__init__(args)
		self.add_variables()
		self.add_optimizer()


	def add_variables(self):

		self.embeddings_char=torch.nn.Embedding(self.char_types,
			50).cuda()

		self.embeddings_build=torch.nn.Embedding(self.build_size,
			200).cuda()

		embeddings_word=torch.cuda.FloatTensor(self.word_embed)
		self.embeddings_word=torch.nn.Embedding.from_pretrained(embeddings_word,
			freeze=True).cuda()


		self.char_lstm=torch.nn.LSTM(input_size=50,
			hidden_size=50,bidirectional=True,batch_first=True).cuda()

		self.lstm1=torch.nn.LSTM(input_size=300,
			hidden_size=100,bidirectional=True,batch_first=True).cuda()

		self.lstm2=torch.nn.LSTM(input_size= 200,
			hidden_size=100,bidirectional=True,batch_first=True).cuda()

		self.linear = torch.nn.Linear( 200, self.args.class_num).cuda()

		self.logloss=torch.nn.BCEWithLogitsLoss()

		dim=200
		self.context1=torch.nn.Parameter(torch.cuda.FloatTensor(
			1,1,dim),
			requires_grad=True)

		self.context2=torch.nn.Parameter(torch.cuda.FloatTensor(
			1,1,dim),
			requires_grad=True)


	def forward(self,feed_dict):
		self.feed_dict=feed_dict
		self.layer1()
		if self.args.run_mode=='train':
			self.loss_layer()

	def layer1(self):
		
		feed_dict=self.convert_data(self.feed_dict)
		l=len(feed_dict['ids'])
		
		sent_vector=[]
		for i in range(l):
			ids={'char': feed_dict['ids_char_pad'][i], 'word':feed_dict['ids'][i], 
				'word_build': feed_dict['ids_b'][i]}

			word_vector=self.lexical_layer(ids)
			# c=(2,1,300)
			o,(h,c)=self.lstm1(word_vector)
			# c1=torch.squeeze(c)
			# vector=torch.cat([c[0],c[1]],dim=-1)
			word_context=torch.mean(o,dim=1,keepdim=True)
			vector,_,_,_=self.attend(self.context1,o)
			# print(vector.size())
			# (2,300)
			# att=c1.view([1,-1])
			sent_vector.append(vector)

		sent_tensor=torch.cat(sent_vector,dim=1)
		# sent_tensor=torch.unsqueeze(sent_tensor,dim=0)

		o,(h,c)=self.lstm2(sent_tensor)
		# vector=torch.cat([c[0],c[1]],dim=-1)
		sent_context=torch.mean(o,dim=1,keepdim=True)
		vector,_,_,_=self.attend(self.context2,o)
		vector=torch.squeeze(vector,dim=0)

		self.prediction=self.linear(vector)


	def loss_layer(self):
		label=self.feed_dict['label']
		l=torch.cuda.FloatTensor(label).view([-1,self.args.class_num])
		self.loss=self.logloss(self.prediction,l)

		


