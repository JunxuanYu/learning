"""
键盘输入小明学习的课程名称及考分等信息，信息间采用空格分隔，每个课程一行，空行回车结束录入，示例格式如下：
数学 90
语文 95
英语 86
物理 84
生物 87
屏幕输出得分最高的课程及成绩，得分最低的课程及成绩，以及平均分（保留2位小数）。
注意，其中逗号为英文逗号，格式如下：
最高分课程是语文95,最低分课程是物理84,平均分是88.40
"""
data = input()#课程名 考分
d = {}
while data:
	ls = data.split(" ")
	d[ls[0]] = int(ls[1])
	data=input()
lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse=True)
avg = sum(d.values()) / len(lt)
print("最高分课程是{}{}，最低分课程是{}{}，平均分是{:.2f}".format(lt[0][0],lt[0][1],lt[-1][0],lt[-1][1],avg))
