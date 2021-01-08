N=int(input())

m= [[0]*10 for _ in range(10)]

for n in range(N):
    for j in range(10):
      if j==n :
        if m[n][j]==1:
          m[n][j]=1
        else:
          m[n][j]=0
      
      elif m[n][j]==1 :
        m[n][j]=0 
      else:
        m[n][j]=1 
        
    for i in range(10):
      if m[i][n]==1:
        m[i][n]=0 
      else:
        m[i][n]=1
        
for i in range(10):
  for j in range(10):
    print(m[i][j],end=' ')
  print()
