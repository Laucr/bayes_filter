import jieba.analyse
from Text_Filter.tf import TextFilter as tf
import os
import collections
import copy
from Logger.logger import Logger as Log
# f = open("b.txt")
# all_text = f.read()
# f.close()
#
# f2 = open("c.txt")
# bll_text = f2.read()
# f2.close()
# s = ''.join(jieba.analyse.textrank(all_text))
# for kw in jieba.analyse.textrank(all_text, topK=5):
# 	print kw
# a = []
# a.append(jieba.analyse.textrank(all_text, topK=5))
# a.append(jieba.analyse.textrank(bll_text, topK=3))
#
# s = ''
# for i in a:
# 	s += ' '.join(i)
# 	s += ' '
# print s

set_files = tf.get_sets(os.path.abspath('./train_set'))
tmp = {}
Log.log('From sort: Military:')
Log.log('Total size:', len(set_files['Military']))


for iter_file in set_files['Military']:
	with open(iter_file) as f:
		all_text = f.read()
		for kw in jieba.analyse.textrank(all_text, topK=50, allowPOS=('ns', 'n')):
			if kw not in tmp:
				tmp[kw] = 0
			tmp[kw] += 1

kw_dic = collections.OrderedDict(sorted((copy.deepcopy(tmp).items()), key=lambda t: -t[-1]))
iter_ = 0
for kw in kw_dic:
	iter_ += 1
	print kw, ': ', kw_dic[kw]*1.0/len(set_files['Government']) * 100, '%'
	if iter_ == 20:
		break

