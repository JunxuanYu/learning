"""
键盘输入一段中文文本，不含标点符号和空格，命名为变量s，采用jieba库对其进行分词，输出该文本中词语的平均长度，保留1位小数。
例如：键盘输入：吃葡萄不吐葡萄皮
屏幕输出：1.6
"""
import jieba
txt = input("请输入一段中文文本：")
ls = jieba.lcut(txt)
print("{:.1f}".format(len(txt)/len(ls)))
