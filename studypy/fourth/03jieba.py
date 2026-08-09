"""
键盘输入一句话，用jieba分词后，将切分的词组按照在原话中逆序输出到屏幕上，词组中间没有空格。示例如下：
输入：
我爱妈妈
输出：
妈妈爱我
"""
import jieba
txt = input("请输入一段中文文本：")
ls = jieba.lcut(txt)
for i in ls[::-1]:
	print(i,end="")
