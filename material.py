# -*- coding:utf-8 -*-
import io
import re
import json
import pickle

freq_map = {}

def getMaterial(line):
	#pieces = re.split(r'[0-9]|[A-Z]|[a-z]|“|”|，|。|：|；|、', line)
	pieces = re.split(r'[0-9A-Za-z“”，。：；、？【】\[\]《》\.（）@%—— ·/！!□■\+\(\)……‘’\-\":\'\,\<\>\?~#①②③④⑤⑥⑦⑧⑨;°℃ \|●&∶～_=]'.decode('utf-8'), line)
	#pieces = re.split(r'，'.decode("utf-8"), line)
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

path = "sina_news/2016-"
num = 1

for num in range(1,12):
	path = "sina_news/2016-%02d.txt" % (num)
	print "processing:"
	print path
	with io.open("sina_news/2016-09.txt", 'r', encoding = "utf-8") as f:
		for eachline in f:
			line = json.loads(eachline)
			#print json.dumps(line, encoding="UTF-8", ensure_ascii=False)
			getMaterial(line["html"])
			getMaterial(line["title"])

with open("freq_map.pickle","wb") as f:
	pickle.dump(freq_map, f)

#print freq_map["心".decode("utf-8")]

#with open("freq_map.pickle","wb") as f:
#		pickle.dump(freq_map, f)