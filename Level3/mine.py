N,M= map(int,input().split())
X,Y = map(int,input().split())

m = [list(map(int,input().split())) for _ in range(N)]
cnt=0 

if m[X-1][Y-1] == 0:
  for i in range(X-2,X+1):
    for j in range(Y-2,Y+1):
      if m[i][j]==1:
        cnt+=1 
  print(cnt)
else:
  print('game over')
