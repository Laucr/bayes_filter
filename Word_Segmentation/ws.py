from Text_Filter.tf import TextFilter as tf
import os
import jieba.analyse
import codecs


train_set_files = tf.get_sets(os.path.abspath('./train_set'))
test_set_files = tf.get_sets(os.path.abspath('./test_set'))


def wd_seg(filename):
	f = open(filename)
	all_text = f.read()
	seg_list = [wd for wd in jieba.analyse.textrank(all_text, topK=25)]
	f.close()
	f = codecs.open(filename + '.txt', 'w', 'utf-8')
	for wd in seg_list:
		if wd != u' ' and wd != u'\n':
			f.write(wd)
			f.write(' ')
	f.close()


def seg_set(set_files):
	files = 0
	for iter_basename in set_files:
		files += len(set_files[iter_basename])
		for iter_filename in set_files[iter_basename]:
			wd_seg(iter_filename)
		print files


seg_set(test_set_files)
seg_set(train_set_files)
