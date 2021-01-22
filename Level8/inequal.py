n = int(input())
signs = input().split()
result=[0]*10
check=[0]*10
a=False

def getMax(x):
  global a
  if a==True:
    return
  if x> n :
    for j in range(n+1):
      print(result[j],end='')
      a=True
   
 
  else:
    for i in range(9,-1,-1):
      result[x]=i
     
      if check[i]==0:
        flag=False
        if(x==0):
         flag=True 
        
        else:
          if 'i' not in result:
          
            if signs[x-1]=='>':
             if result[x-1] > result[x]:
              
              flag=True
            
            else:
              if result[x-1] < result[x]:
                flag=True
           
        if flag==True:
          check[i]=1
          getMax(x+1)
          check[i]=0
 
          
def getMin(x):
  global a
  if a==True:
    return
  if x> n :
    for j in range(n+1):
      print(result[j],end='')
      a=True
   
 
  else:
    for i in range(10):
      result[x]=i
     
      if check[i]==0:
        flag=False
        if(x==0):
         flag=True 
        
        else:
          if 'i' not in result:
          
            if signs[x-1]=='>':
             if result[x-1] > result[x]:
              
              flag=True
            
            else:
              if result[x-1] < result[x]:
                flag=True
           
        if flag==True:
          check[i]=1
          getMin(x+1)
          check[i]=0
  

getMax(0)
getMin(0)
