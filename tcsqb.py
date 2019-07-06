import math

nos=int(input())
a=[]
for i in range(nos):
		x=int(input())
		y=math.log(x,2)
		a+=[int(y)+1]

for i in a:
	print(i)
