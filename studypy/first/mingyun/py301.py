"""
对“命运.txt”文件进行字符频次统计，输出频次最高的中文字符（不包含标点符号)及其频次，字符与频次之间采用英文冒
号”：“分隔，示例格式如下：
理:224
"""
f = open("命运.txt",'r')
txt = f.read()
d = {} # 存放统计结果
for i in  txt:
	if i not in "，。？《》--【】、！；“”‘’：（）\n":
	# 对每一个字符统计它的数量
		d[i] = d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)

print("{}:{}".format(ls[0][0],ls[0][1]))

f.close()
