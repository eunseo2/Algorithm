
N= int(input())
a=1
k=1 

for i in range(N):
  if a >= N:
    break
  else:
    a+= 6*i
    k=i+1
    
    
print(k)
