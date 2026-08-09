f = open("PY301-SunSign.csv",'r')

ls = []
s = input("请输入星座中文名称（例如：双子座）：")
lt = f.readlines()
for line in lt:
	ls = line.strip('\n').split(',')
	if ls[1] == s:		
		print（"{}的生日位于{}-{}之间".format(ls[1],ls[2],ls[3]))
f.close()
