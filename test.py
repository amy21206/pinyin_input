# -*- coding:utf-8 -*-
import pickle
import io

pinyin_map = {}
pinyin_list = []
list12 = []

with open('pinyin_map.pickle','rb') as f:
	pinyin_map = pickle.load(f);
with open('pinyin_list.pickle','rb') as f:
	pinyin_list = pickle.load(f);

wordlist = ""

with io.open('characters/12hanzi.txt', 'r', encoding = 'gbk') as f:
	for line in f:
		wordlist = line.encode("gbk").decode("gbk").encode("utf8")
		print len(wordlist)/3

for i in range(len(wordlist)/3):
	w = wordlist[3*i:3*i+3]
	list12.append(w)

cnt = 0

for pinyin in pinyin_list:
	for word in pinyin_map[pinyin]:
		if word in list12:
			cnt += 1

print cnt
		#	print word