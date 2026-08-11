import jieba
f = open('out1.txt','w')
fi = open('data.txt','r')
ls = fi.readlines()
D = []
for line in ls:
    wordlist = jieba.lcut(line)
    for word in wordlist:
        if len(word) >= 3 and word not in D:
            D.append(word)
f.write('\n'.join(D))
f.close()
fi.close()