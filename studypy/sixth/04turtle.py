'''
使用turtle库的turtle.fd()函数和turtle.seth()函数绘制一个边长为100像素的正五边形
'''
import turtle
turtle.pensize(2)
d = 0
for i in range(1,6):
    turtle.fd(100)
    d += 72  
    turtle.seth(d)