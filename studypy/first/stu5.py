"""
键盘输入一组人员的姓名、性别、年龄等信息，信息间采用空格分隔，每人一行，空行回车结束录入，示例格式如下：
张三 男 23
李四 女 21
王五 男 18
计算并输出这组人员的平均年龄（保留2位小数）和其中男性人数，格式如下：
平均年龄是20.67男性人数是2
"""
data = input()#姓名 年龄 性别
age = 0
s = 0
man_num = 0
while data:
	ls = data.split(" ")
	age = age + int(ls[2])
	s += 1
	if ls[1] == '男':
		man_num += 1
	data = input()
ave = age / s
print("平均年龄是{:.2f}男性人数是{}".format(ave,man_num))
