"""
以100为随机数种子，随机生成3个在1(含）到9(含）之间的随机整数，计算这三个随机整数的立方和。
"""
import random
random.seed(100)
s = 0
for i in range(3):
    n = random.randint(1,9)
    s = s + n**3
print(s)