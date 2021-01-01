N=int(input())
cnt=0

arr=[[0]*N for _ in range(N)]

for i in range(N):
  x=0
  y=i
  for j in range(i+1):
      cnt+=1
      arr[x][y]= cnt
      x+=1
      y-=1
      
for i in arr:
  for j in i:
    if j!=0:
      print(j, end=' ')
  print()
