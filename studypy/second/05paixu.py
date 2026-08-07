"""
键盘输入某班各个同学就业的行业名称，行业名称之间用空格间隔（回车结束输入）。完善Python代码，统计各行业就业的学生数量，按数量从高到低方式输出。例如输入：
交通 金融 计算机 交通 计算机 计算机
输出参考格式如下，其中冒号为英文冒号：
计算机：3
交通：2
金融：1
"""
names = input("请输入各个同学行业名称，行业名称之间用空格间隔(回车结束输入)")
ls = names.split()
d= {}
for i in ls:
	d[i] = d.get(i,0)+1
	
ls=list(d.items ())
ls.sort(key = lambda x:x[1], reverse = True)#按照数量排序
for k in ls:
	print("{}:{}".format(k[0],k[1]))
