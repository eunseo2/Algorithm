
result=[]

cnt=0
def divison(x,d):
 
  if x>= n:
    global cnt
    cnt+=1
    print(result[0],end='')
    for i in range(1,len(result)):
      print('+'+str(result[i]),end='')
    print()  
   
  else:
    num=0
    if x==0:
      num=n-1
      
    else:
      num=n-x
     
    for i in range(num,0,-1):
      result.append(i)
      if d>0 and result[d-1]<result[d]:
        result.pop()
        continue
      divison(x+i,d+1)
      result.pop()
      
    
 
n=int(input())    
divison(0,0)
print(cnt)
