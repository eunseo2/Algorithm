N=int(input())

d= [[0]*N for _ in range (N)]

x,y,r =map(int,input().split())

a = 0

for i in range(0,N):
  for j in range(0,N): 
    a=abs(x-1-i)+abs(y-1-j)
    if a<=r :
      d[i][j]=a
    else:
      d[i][j]=0
    
    if i+1==x and j+1==y :
      d[i][j]='x'   
for i in range(0,N):
  for j in range(0,N):
    print(d[i][j],end=' ')
  print()
