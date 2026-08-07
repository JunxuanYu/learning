fi = open("论语.txt",'r')
fo = open("论语-原文.txt",'w')
flag = False

for line in fi:
	if '【原文】' in line:
		flag = True
		continue
	if '【注释】' in line:
		flag = False
	line = line.strip("\n")
	if flag == True:
		if line:
			fo.write(line+'\n')	
fi.close()
fo.close()
