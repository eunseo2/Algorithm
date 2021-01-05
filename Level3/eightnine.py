N,M = map(int, input().split())

a=[list(map(int, input().split())) for _ in range(N)]

b= a.copy()

#import copy
#b= copy.deepcopy(a)

for i in range(N):
  for j in range(M):
    b[i][j] = a[i][M-j-1]
    print(b[i][j],end=' ')
  print()
