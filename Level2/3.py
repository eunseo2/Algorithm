N= int(input())

lst = list(map(int,input().split()))

sum=0
cnt=0 

for i in range(0,N):
  if lst[i]==1:
    cnt+=1
    sum+=cnt
  else:
    cnt=0
      
print(sum)
