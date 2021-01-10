def check():
  sum=0
  for i in range(M):
    cnt=0
    for j in range(N):
      if m[i][j]==1:
        cnt+=1 
    if cnt==N:
      sum+=1

  return sum  
  
N,M= map(int,input().split())

m= [list(map(int,input().split())) for _ in range (M)]


max1=0
max_i=0
sum2=0

for i in range(M-1,-1,-1):
  for j in range(N-1,-1,-1):
    if i >= 3 : 
      if m[i][j]==0 and m[i-1][j]==0 and m[i-2][j]==0 and m[i-3][j]==0:
        k1=j
        k2=i
        m[i][j]=1
        m[i-1][j]=1
        m[i-2][j]=1
        m[i-3][j]=1
        sum2= check() 
        
        
        if max1 < sum2 :
          max1 = sum2
          max_i = j+1
        
        m[i][j]=0
        m[i-1][j]=0
        m[i-2][j]=0
        m[i-3][j]=0



print(max_i,max1)
