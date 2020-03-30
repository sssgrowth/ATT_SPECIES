import os
import sys
sys.path.append('..')
from utils.util import *
import operator
from service.process import *

class load_embeddings(object):
	def __init__(self,args):
		# self.config=Config()
		self.args=args
		self.process=Process(args)
		self.util=Util()

	def load_pretrained_word_embedding(self,pre_char=False):

		h5=self.util.load_data_from_h5(self.args.word_embeding_path)
		word_embed=np.array(h5['word_embedding'])
		pkl=self.util.load_data_from_pkl(self.args.vocab_path)
		word_vocab=pkl['vocab']
		v_ix,embed=self.process.complement_embedding(word_vocab,word_embed,word_embed.shape[1])
		charcab=self.util.read_to_list(self.args.charcab_path,trim=True)
		
		# it contains _PAD _UNK in charcab
		c_ix={c:i for i,c in enumerate(charcab)}
		return embed,None,v_ix,c_ix
		

	def load_build_vocab(self):
		pkl=self.util.load_data_from_pkl(self.args.build_vocab)
		word_vocab=pkl['vocab']
		# word_vocab=sorted(word_vocab.items(), key=operator.itemgetter(1))
		word_vocab=sorted(word_vocab)
		w_ix={v:k+4 for k,v in enumerate(word_vocab)}
		
		w_ix['_PAD']=0
		w_ix['_UNK']=1
		w_ix['_SAT']=2
		w_ix['_EOS']=3

		return w_ix