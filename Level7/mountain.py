def mountain(N):
  if N==1:
    print(1,end='')
  else:
    
    mountain(N-1)
    print(N,end='')
    mountain(N-1)
    
  


N=int(input())
mountain(N)
