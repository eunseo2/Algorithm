N=int(input())
b= list(map(int,input().split()))
a=[0]*N 

for i in range(N):
  
  if i==0:
    a[i]=b[i]
    print(a[i],end=' ')
    
  else:
    a[i]=b[i]*(i+1)
    for j in range(i):
      a[i]-=a[j]
    print(a[i],end=' ')
