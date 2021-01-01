A= list(map(int,input().split()))
B= list(map(int,input().split()))
acount=0 
bcount=0 
count=0

for i in range (0,10):
  if A[i]> B[i]:
    acount+=1
  elif A[i]<B[i]:
    bcount+=1
  else:
    A[i]==B[i]
    count+=1


if acount > bcount :
  print('A')
elif acount < bcount :
  print('B')
else:
  print('D')
