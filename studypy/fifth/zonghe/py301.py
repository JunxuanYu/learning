mport jieba
f= open('data.txt','r')
lines=f.readlines()
f. close()
f = open('out. txt','w')
for line in lines:
	line = line.strip('')
	wordList = jieba.lcut(line)
	f.writelines('\n'.join(wordList))
f.close()
