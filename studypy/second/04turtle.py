"""
使用turtle库的turtle.fd()函数和turtle.seth()函数绘制一个边长为200的正菱形，菱形4个内角均为90度。
"""
import turtle
turtle.pensize(2)
d = -45
for i in range(4):
	turtle.seth(d)
	d += 90
	turtle.fd(200)
