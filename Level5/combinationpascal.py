n,r=map(int,input().strip().split())

d=int(n+1)

a = [[0]*d for _ in range (d)]


for i in range (d) :
  a[i][0]=1
  for j in range (1,i+1):
    a[i][j]=a[i-1][j-1]+a[i-1][j]
  
print(a[n][r])
