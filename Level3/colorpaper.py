N=int(input())
cnt=0 
arr = [[0]*101 for _ in range(101)]

for i in range(1,N+1):
  xi,yi,bi,zi = map(int,input().split())
 
  for j in range(xi,xi+bi):
    for k in range(yi,yi+zi):
      arr[j][k]=i
      


for i in range(1,N+1):
  for j in range(101):
    for k in range(101):
      if arr[j][k]==i :
          cnt+=1 
  print(cnt)
  cnt=0
    
