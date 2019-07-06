mod=1000000007
def factmod(n):
	f=1
	modv=[1]
	for i in range(1,n+1):
		f=f*i%mod
		modv+=[f]
	return modv


n = int(input())
a = list(map(int,input().split()))
q = int(input())
lr=[]
for i in range(q):
	lr+=[list(map(int,input().split()))]


modv=factmod(max(a))

facta=[]
for i in range(n):
	facta+=[modv[a[i]]]


cf=[facta[0]]
for i in range(n):
	cf+=[cf[-1]*facta[i]]


for l,r in lr:
	p=(cf[r]//cf[l-1])%mod
	pp=1
	for i in range(0,r-l):
		pp=(pp*p)%mod
	print(pp)


