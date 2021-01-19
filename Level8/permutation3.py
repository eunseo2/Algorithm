def getResult(x):
  if x>=r :
    for i in range(0,r):
      print(chr(result[i]+ord('a')),end='')
    print()
    return
    
  else:
    for i in range(n):
      if check[i]==0: 
        result.append(i)
        check[i]=1
        getResult(x+1)
        # x번째에 i를 넣는 모든 경우를 이미 다 고려
        check[i]=0
        result.pop()
        
n,r=map(int,input().split())
result=[]
check= [0]*n

getResult(0)
