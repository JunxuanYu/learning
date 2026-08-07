"""
使用turtle库的turtle.fd()函数和turtle.seth()函数绘制一个每方向为100像素长度的十字形
"""
import turtle
for i in range(4):
	turtle.fd(100)
	turtle.fd(-100)
	turtle.seth((i+1)*90)

