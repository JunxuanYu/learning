"""
45、使用字典和列表型变量完成村长选举。某村有40名有选举权和被选举权村民名单由考生文件夹下文件name.txt给出，从这40名村民中选出一人当长，40人
的投票信息由考生文件夹下文件vote.txt给出，每行是一张选票的信息，有效票中得票最多的村民当选。
问题1：请从vote.txt中筛选出无效票写入文件vote1.txt。有效票的含义是：选票中只有一个名字且该名字在name.txt文件列表中，不是有效票的票称为无效票。
问题2：给出当选村长的名字及其得票数。
在考生文件夹下给出了程序框架文件PY202.py.补充代码完成程序。
"""
f = open('name.txt')
names = f.readlines()
f.close()
f = open('vote.txt')
votes = f.readlines()
f.close()
f.close()
f = open('vote1.txt','w')
D = {}
NUM = 0
for vote in votes :
	num = len(vote.split())
	if num == 1 and vote in names:
		D[vote[:-1]] = D.get(vote[:-1],0)  + 1
		NUM += 1
	else:
		f.write(vote)
f.close()
l = list(D.items)
l.sort(key = lambda s:s[1],severse=True )
name = l[0][0]
score = l[0][1]
print("有效票数为：{}，当选村长的村民为：{}，票数为：{}".format(NUM,name,score))
		
