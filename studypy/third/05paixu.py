"""
键盘输入一组我国高校所对应的学校类型，以空格分隔，共一行，示例格式如下：
综合 理工 综合 综合 综合 师范 理工
统计各类型的数量，从数量多到少的顺序屏幕输出类型及对应数量，以英文冒号分隔，每个类型一行，输出参考格式如下：
综合:4
理工:2
师范:1
"""
txt=input("请输入类型序列：")
lt = txt.split(" ")
d= {}
for i in lt:
	d[i]=d.get(i,0)+1
ls =list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)#按照数量排序
for k in ls:
	print("{}: {}".format(k[0], k[1]))
