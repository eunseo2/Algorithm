N = int(input())

for i in range(1,10000+1):
  if (i-1)*(i-1) < N and i*i >= N :
           print(i)
