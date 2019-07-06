mod = 1000000007
x = int(input())
memo = [1,0]
l=1
if x<=1:
	print(memo[x])

if 250000<x:
	pass
if 500000<x:
	pass
if 750000<x:
	pass

while l<x:
	temp=(memo[0]+memo[1])*l%mod
	l+=1
	memo[0],memo[1]=memo[1],temp

print(memo[1]%mod)