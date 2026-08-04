"""
随机选择——个手机品牌屏幕输出。
"""
import random
brandlist = ["华为","苹果","诺基亚","OPPO","小米"]
random.seed(0)
name = random.choice(brandlist)
print(name)
