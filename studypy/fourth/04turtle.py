"""
使用turtle库的turtle.fd()函数和turtle.seth()函数绘制一个等边三角形，边长为200像素，效果如下图所示。
"""
import turtle as t 
for i in range(3):
	t.seth(i*120)
	t.fd(200)
