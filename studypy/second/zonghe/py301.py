f = open("sensor.txt","r",encoding="utf-8")
fo = open("earpa001.txt",'w')
ls = f.readlines()
for line in ls:
	lt = line.strip("\n").split(',')
	if lt[1] == ' earpa001':
		fo.write("{},{},{},{}\n".format(lt[0],lt[1],lt[2],lt[3])) 

f.close()
fo.close()
