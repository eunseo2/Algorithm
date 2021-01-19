def getResult(x):
  
  if x>=r :
    flag=False
    for i in range(r):
      for j in range(r):
        if i!=j and result[i]==result[j]:
          flag=True
    
    if flag== False:    
      for i in range(r):
        print(chr(result[i]+ord('a')),end='')
      print()
    
  else:
    for i in range(n):
      result[x]=i
      getResult(x+1)
      
n,r=map(int,input().split())
result=[0]*r

getResult(0)
