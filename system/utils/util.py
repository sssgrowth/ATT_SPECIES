#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('..')
import h5py
import pickle
import numpy as np
import csv
class Base_util(object):

	def read_to_list(self,file,trim=False):
		with open(file,'r') as f:
			l=f.readlines()
			if trim==True:
				l=[x.strip() for x in l if x.strip()!='']
		# return [e for e in l]
		return l

	def write_file(self,s,path):
		with open(path,'wb') as f:
			f.write(s)

	def read_file(self,path):
		with open(path,'rb') as f:
			s= f.read()
		return s.decode('utf-8')

	def append_file(self,s,path):
		with open(path,'ab+') as f:
			f.write(s)

	def list_files_dir(self,path,suffix):
		result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) 
			for f in filenames if os.path.splitext(f)[1] == suffix]
		return result


class Util(Base_util):
	def __init__(self):
		super(Util,self).__init__()

