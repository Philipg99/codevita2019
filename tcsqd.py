d=[0,31,28,31,30,31,30,31,31,30,31,30,31]

demand=[0]
for i in range(1,13):
	for j in  range(1,d[i]+1):
		demand+=[abs(j-15)+((6-i)**2)]



rooms = int(input())
tv,ntv = list(map(int,input().split()))
goal = int(input())
flg=0
tvs=0
while tvs<=rooms:
	tot=0
	for i in demand:
		tot+=min(i,rooms-tvs)*ntv
		tot+=min(max(i-rooms+tvs,0),tvs)*tv

	if tot>=goal:
		print(tvs)
		flg=1
		break
	else:
		tvs+=1
if flg==0:
	print(rooms)