import os
import sys
sys.path.append('..')
import torch
import numpy as np
from utils.util import *
from sklearn.metrics import hamming_loss
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score,recall_score,precision_score,classification_report
import mmap
import random
import time

class Load_data(object):

	def __init__(self,args=None):
		self.util=Util()
		self.args=args
		self.reflect_class()

	def reflect_class(self):
		clazz=self.util.read_to_list(self.args.class_config,trim=True)
		if self.args.model_name in ['Gen']:
			clazz=['O\tO']+clazz
		dct={}
		for i,l in enumerate(clazz):
			arr=l.split('\t')
			dct[arr[0]]=i
		self.class_list={i:spc for spc,i in dct.items()}
		self.class_dct=dct
		self.class_num=len(dct)

	def convert_pubmed(self,s):
		# s=f_handler.readline()
		# yield s
		arr=s.split('\t')
		text=arr[-1].strip()
		label=[0]*len(self.class_dct)
		animals=arr[0].split('@@@')
		if len(animals)==0:
			label[0]=1
			label=np.array(label)
		else:
			for a in animals:
				print('animals>>',a)
				label[self.class_dct[a]]=1
			label=np.array(label)
		pmid="0"
		feed_dict={'text':text,'label':label,'pmid':arr[1].strip()}

		return feed_dict

	def eval_data(self,y,t):
		for y1,t1 in zip(y[:10],t[:10]):
			# print(zip(y1,t1))
			tm=[]
			for i in range(t1.shape[-1]):
				tm.append((y1[i],t1[i]))
			print(tm)
		
		y=np.array(y)
		t=np.array(t)

		if self.args.model_name in ['Gen']:
			# remove the 'O' class
			y=y[:,1:]
			t=t[:,1:]

		logloss=log_loss(t,y)

		# logloss=self.mylogloss(t,y)
		print ('log: ', logloss)
		print ("!note what is your threshold!")
		y_hat=y>0.5
		# print y_hat.size()
		y_hat=np.array(y_hat,dtype=np.int32)

		print('saving result')
		self.util.write_file("".encode('utf8'),self.args.output_result)
		for y1,t1 in zip(y_hat,t):
			# print(zip(y1,t1))
			predline=[]
			groundline=[]
			if self.args.model_name in ['Gen']:
				for i in range(self.class_num-1):
					# tm.append((y1[i],t1[i]))
					if y1[i]==1:
						pred=self.args.class_list[i+1]
						predline.append(pred)
					if t1[i]==1:
						ground=self.args.class_list[i+1]
						groundline.append(ground)
			else:
				for i in range(self.class_num):
					# tm.append((y1[i],t1[i]))
					if y1[i]==1:
						pred=self.args.class_list[i]
						predline.append(pred)
					if t1[i]==1:
						ground=self.args.class_list[i]
						groundline.append(ground)
			meg=[predline,groundline]
			self.util.append_file("{}\n".format(meg).encode('utf8'),self.args.output_result)
		
		f1=f1_score(t,y_hat,average='micro')
		recall=recall_score(t,y_hat,average='micro')
		precision=precision_score(t,y_hat,average='micro')
		print('cac f1:',2*recall*precision/(recall+precision))
		ham=hamming_loss(t,y_hat)
		
		# roc_auc=hamming_loss(t,y)
		s='logloss: {}; micro f1: {}; hamming loss: {} precision: {} recall: {}\n'.format(logloss,
			f1,
			ham,
			precision,
			recall)
		print (s)

		report=classification_report(t,y_hat,digits=5)
		print('class report',report)

		docLevelRes={'r':[],'p':[],'f1':[]}

		def prf(t,y):
			p=np.sum(t*y)/(np.sum(y)+1e-6)
			r=np.sum(t*y)/(np.sum(t)+1e-6)
			f=2*p*r/(p+r+0.000001)
			return p,r,f

		for i in range(y_hat.shape[0]):
			k=t[i]
			v=y_hat[i]
			p,r,f=prf(k,v)
			# recall=recall_score(k,v,average='micro')
			# precision=precision_score(k,v,average='micro')
			# f1=f1_score(k,v,average='micro')
			docLevelRes['r'].append(r)
			docLevelRes['p'].append(p)
			docLevelRes['f1'].append(f)
		print(docLevelRes)
		print('document level result: p {} r {} f {}'.format(np.mean(docLevelRes['p']),
			np.mean(docLevelRes['r']),
			np.mean(docLevelRes['f1'])))

		self.util.append_file(s.encode('utf8'),self.args.test_log)
		return logloss,f1,ham