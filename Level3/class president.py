n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
cnt=0
lst=[]

for i in range(n):
  for j in range(n):
    for k in range(5):
      if i!=j :
        if arr[i][k]==arr[j][k]:
          cnt+=1
          break
  
  lst.append(cnt)  
  cnt=0

for i in range(n):
  if lst[i]==max(lst):
    print(i+1)
    break


   
