f = open('PY301-SunSign.csv','r')
ls = []
lt = f.readlines()
while True:
	s = input("请输入星座序号（例如，5）：")
	for i in s.split(''):
		for line in lt:
			ls = line.strip('\n').split(',')
			if ls[0] == i:
				print("{}({})的生日是{}月{}日至{}月{}日之间".format(ls[1],ls[4],ls[2][:-2],ls[2][-2:],ls[3][:-2],ls[3][-2:]))
f.close()
