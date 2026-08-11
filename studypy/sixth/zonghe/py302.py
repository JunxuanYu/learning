import jieba
f = open('out2.txt','w')
fi = open('data.txt','r')
lt = fi.readlines()
d = {}
for line in lt:
    wordlist = jieba.lcut(line.strip('\n'))
    for word in wordlist:
        if len(word) >= 3:
            d[word] = d.get(word,0) + 1
ls = list(d.items())
ls.sort(key = lambda x:x[1],reverse = True)
for i in ls:
    f.write("{}:{}".format(i[0],i[1])+'\n')
f.close()
fi.close()
