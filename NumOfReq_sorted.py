f  = open("/var/log/nginx/access.log")
f = f.readlines()
dic = {}

for i in f:
	url = i.split(" ")[6]
	if url in dic.keys():
		dic[url] += 1
	else:
		dic[url] = 1

for key, value in sorted(dic.items(), key = lambda item: item[1], reverse = True):
	print("{} => {}".format(key, value))
