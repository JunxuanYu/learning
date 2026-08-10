"""
以0为随机数种子，随机生成5个在1（含）到97（含）之间的随机数，计算这五个随机数的平方和。
"""
import random
random.seed(0)
s =0
for i in range(5):
	n = random.randint(1,97)# 产生随机数
	s = s + n**2
print(s)
