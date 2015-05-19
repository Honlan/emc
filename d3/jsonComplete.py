# coding:utf-8
import json

fr = file("test.json", "r")
fw = file("out.json", "w")
s = json.load(fr)

for item in s:
	parent = item["imports"][0]
	haveFind = False
	for i in s:
		if i['name'] == parent:
			haveFind = True
			break
	if not haveFind:
		print "action!"
		# s.append("{'name': '" + parent + "', 'imports': []}")


json.dump(s, fw)

fr.close()
fw.close()