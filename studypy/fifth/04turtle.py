"""
使用turtle库的turtle.fd0函数和turtle.seth0函数绘制一个边长为100的正八边形，在考生文件夹下给出了程序框架文件PY201.py，在横线处补充代码，不得修改其它代码。效果如下图所示。
"""
import turtle
turtle.pensize(2)
d = 0
for i in range(1,9):
	turtle.fd(100)
	d += 45
	turtle.seth(d)
