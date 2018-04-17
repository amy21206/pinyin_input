# -*- coding:utf-8 -*-
import io
import pickle

a = 0;

pinyin_map = {}
pinyin_list = []

cnt = 0

with io.open('characters/pinyin.txt', 'r', encoding = 'gbk') as f:
	print "opened"
	for eachline in f:
		words = ( eachline.encode("gbk").decode("gbk").encode("utf8") ).split()
		if len(words) > 0:
			pinyin_map[words[0]] = words[1:]
			pinyin_list.append(words[0])
			cnt += len(pinyin_map[words[0]])
			print words[0]
			#for eachword in pinyin_map[words[0]]:
			#	print eachword.decode("utf8").encode("utf8")
			#	#print eachword
			#print "xxxxxxxxxxxxxxxxxxxxxxxx"

'''for eachword in pinyin_map["ang"]:
	print eachword
'''
with open('pinyin_map.pickle','wb') as f:
	pickle.dump(pinyin_map, f)
with open('pinyin_list.pickle','wb') as f:
	pickle.dump(pinyin_list, f)

print cnt