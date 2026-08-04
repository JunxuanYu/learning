"""
对“命运，txt”文件进行字符频次统计，按照频次由高到低，屏幕输出前10个频次最高的字符，不包含回车符，字符之间无间隔，连续输出，示例格式如下：
理斯卫...(后略，共10个字符）
"""
f = open("命运.txt",'r')
txt = f.read()
d = {} # 存放统计结果
for i in  txt:
	if i not in "\n":
	# 对每一个字符统计它的数量
		d[i] = d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
	print(ls[i][0],end="")

f.close()
