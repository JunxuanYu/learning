"""
对“命运.txt”文件进行字符频次统计，将所有字符按照频次从高到低排序，字符包括中文、标点、英文等符号，但不包含空格和回车。将排序后的字符及频次输出到考生文件夹下，文件名为“命运-频次排序，tx”。字符与频次之间采用英文冒号”：分隔，各字符之间采用英文逗号”：分隔，参考CSV格
式，最后无逗号，文件内部示例格式如下：
理:224,斯:120,卫:100
"""
f = open("命运.txt",'r')
fo = open("命运—频次排序.txt",'w')
txt = f.read()
d = {} # 存放统计结果
for i in  txt:
        if i not in " \n":
        # 对每一个字符统计它的数量
                d[i] = d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
s = ''
for k in ls:
	s = s + "{}:{},".format(k[0],k[1])
fo.write(s[:-1])
f.close()
fo.close()
