fi = open("论语-原文.txt",'r')
fo = open("论语-提纯原文.txt","w")
for line in fi:
	for i in range(23):
		line=line.replace("（"+str(i)+"）","")
	fo.write(line)

fi.close()
fo.close()
