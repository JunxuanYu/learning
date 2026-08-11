"""
以123为随机数种子，随机生成10个在1(含）到999(含）之间的随机数，每个随机数后跟随——个逗号进行分隔，厅幕输出这10个随机数。
"""
import random
random.seed(123)
for i in range(10):
    print(random.randint(1,999),end=',')