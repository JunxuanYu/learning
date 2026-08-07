f = open('earpa001.txt','r',encoding='utf-8')
fo = open('earpa001_count.txt','w')
ls = f.readlines()
d = {}
for line in ls:
	lt = line.strip('\n').split(',')
	key = lt[2]+'-'+lt[3]
	d[key] = d.get(key,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse = True)
for k in ls:
	fo.write("{},{}\n".format(k[0],k[1]))
f.close()
fo.close()
