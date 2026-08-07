"""
从键盘输入4个数字，各数字采用空格分隔，对应为变量x0,y0,x1.y1。计算两点（x0,y0）和（x1,y1)之间的距离，屏幕输出这个距离，保留2位小数。
例如：键盘输入：0 1 3 5
屏幕输出：5.00
"""
ntxt=input("请输入4个数字（空格分隔）：")
nls = ntxt.split(" ")
x0 = eval(nls[0])
y0= eval(nls[1])
xl = eval(nls[2])
yl = eval(nls[3])
r =pow(pow(xl-x0, 2) + pow(yl-y0, 2),0.5 )
print("{:.2f}". format (r))
