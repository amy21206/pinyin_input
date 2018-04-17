# -*- coding:utf-8 -*-

import io
import re
import json
import pickle

freq_map = {}

with open("freq_map.pickle","rb") as f:
	freq_map = pickle.load(f)

def getMaterial(line):
	#pieces = re.split(r'[0-9]|[A-Z]|[a-z]|“|”|，|。|：|；|、', line)
	pieces = re.split(r'[0-9A-Za-z“”，。：；、？【】\[\]《》\.（）@%—— ·/！!□■\+\(\)……‘’\-\":\'\,\<\>\?~#①②③④⑤⑥⑦⑧⑨;°℃ \|●&∶～_=　０１２３４５６７８９－．，／＼［］｜]'.decode("utf-8"), line)
	for p in pieces:
		if p != "":
			for i in range(len(p)):
				c = p[i]
				if c not in freq_map:
					freq_map[c] = 1
				else:
					freq_map[c] += 1
				w = p[i : i + 2]
				if w not in freq_map:
					freq_map[w] = 1
				else:
					freq_map[w] += 1
			#print len(p)
			#print p.encode("utf-8")

for num in range(1,12):
	path = "sina_news_gbk/2016-%02d.txt" % (num)
	print "processing:"
	print path
	with io.open("sina_news_gbk/2016-09.txt", 'r', encoding = "gbk") as f:
		for eachline in f:
			line = json.loads(eachline)
			#print json.dumps(line, encoding="gbk", ensure_ascii=False)
			try:
				getMaterial(line["html"].encode("gbk").decode("gbk").encode("utf8").decode("utf8"))
			except:
				print "error in 41"
			try:
				getMaterial(line["title"].encode("gbk").decode("gbk").encode("utf8").decode("utf8"))
			except:
				print "error in 45"

with open("freq_map_after_gbk.pickle","wb") as f:
	pickle.dump(freq_map, f)