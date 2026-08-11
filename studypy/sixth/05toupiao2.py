f = open("vote.txt")
names =f.readlinesO
f.close0
D = {}
for name in names:
    if len(name.split()) == 1:
        D[name[:-1]] = D.get(name[:-1],0)+1
l =list (D.items())
l.sort(key=lambda s:s[1],reverse = True)
name =l[0][0]
score =l[0][1]
print("最具人气明星为：{}，票数为：{}".format(name,score))