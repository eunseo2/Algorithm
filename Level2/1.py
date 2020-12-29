n,m=map(int,input().split())


for i in range(n,m+1):
  if i== 2:
      print('2',end=' ')
  for j in range(2,i):
    if i%j==0:
        break
    if i-1==j:
      print(i,end=' ')
