def kight(x,y):
		if 0<= x+2 < n and 0<= y+1 < n:
			if b[x+2][y+1]!=2:
				b[x+2][y+1]=1
		if 0<= x+2 < n and 0<= y-1 < n:
			if b[x+2][y-1]!=2:
				b[x+2][y-1]=1
		if 0<= x-2 < n and 0<= y+1 < n:
			if b[x-2][y+1]!=2:
				b[x-2][y+1]=1
		if 0<= x-2 < n and 0<= y-1 < n:
			if b[x-2][y-1]!=2:
				b[x-2][y-1]=1

		if 0<= x+1 < n and 0<= y+2 < n:
			if b[x+1][y+2]!=2:
				b[x+1][y+2]=1
		if 0<= x-1 < n and 0<= y+2 < n:
			if b[x-1][y+2]!=2:
				b[x-1][y+2]=1
		if 0<= x+1 < n and 0<= y-2 < n:
			if b[x+1][y-2]!=2:
				b[x+1][y-2]=1
		if 0<= x-1 < n and 0<= y-2 < n:
			if b[x-1][y-2]!=2:
				b[x-1][y-2]=1


def bishop(x,y):
		f1,f2,f3,f4=0,0,0,0
		for i in range(1,n):
			if not f1:
				if x+i<n and y+i <n:
					if b[x+i][y+i]!=2:
						b[x+i][y+i]=1
					else:
						f1=1

			if not f2:
				if x+i<n and y-i >=0:
					if b[x+i][y-i]!=2:
						b[x+i][y-i]=1
					else:
						f2=1

			if not f3:
				if x-i >=0 and y+i <n:
					if b[x-i][y+i]!=2:
						b[x-i][y+i]=1
					else:
						f3=1

			if not f4:
				if x-i >=0 and y-i >=0:
					if b[x-i][y-i]!=2:
						b[x-i][y-i]=1
					else:
						f4=1

def rook(x,y):
		for i in range(x+1,n):
			if b[i][y]==2:
				break
			else:
				b[i][y]=1
		for i in range(x-1,-1,-1):
			if b[i][y]==2:
				break
			else:
				b[i][y]=1

		for i in range(y+1,n):
			if b[x][i]==2:
				break
			else:
				b[x][i]=1
		for i in range(y-1,-1,-1):
			if b[x][i]==2:
				break
			else:
				b[x][i]=1

def queen(x,y):
	rook(x,y)
	bishop(x,y)

n = int(input())
b=[]
for i in range(n):
	t=[]	
	for j in range(n):
		t+=[0]

	b+=[t]
bloc=[]
rloc=[]
kloc=[]
qloc=[]
k=int(input())
if k!=0:
	for i in range(k):
		x,y=input().split()
		x,y=int(x),int(y)
		b[x][y]=2	
		kloc+=[[x,y]]


r=int(input())
if r!=0:
	for i in range(r):
		x,y=input().split()
		x,y=int(x),int(y)
		b[x][y]=2
		rloc+=[[x,y]]


bsh=int(input())
if bsh!=0:
	for i in range(bsh):
		x,y=input().split()
		x,y=int(x),int(y)
		b[x][y]=2
		bloc+=[[x,y]]

q=int(input())
if q!=0:
	for i in range(q):
		x,y=input().split()
		x,y=int(x),int(y)
		b[x][y]=2
		qloc+=[[x,y]]

for x,y in kloc:
	kight(x,y) 
for x,y in bloc:
	bishop(x,y) 
for x,y in rloc:
	rook(x,y) 
for x,y in qloc:
	queen(x,y) 


c=0
for i in range(n):
	for j in range(n):
		if b[i][j]==0:
			c+=1
print(c)