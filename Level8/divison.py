
result=[]

cnt=0
def divison(mySum,index):
 
  if mySum>= n:
    global cnt
    cnt+=1
    print(result[0],end='')
    for i in range(1,len(result)):
      print('+'+str(result[i]),end='')
    print()  
   
  else:
    num=0
    if index==0:
      num=n-1
      
    else:
      num=n-mySum
     
    for i in range(num,0,-1):
      result.append(i)
      if index>0 and result[index-1]<result[index]:
        result.pop()
        continue
      divison(mySum+i,index+1)
      result.pop()
      
    
 
n=int(input())    
divison(0,0)
print(cnt)
