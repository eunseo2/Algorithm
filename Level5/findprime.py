N = int(input())
cnt=0
while (N>0):
  n = int(input())
  
  flag=False
  if n==1:
    flag=True 
  

  for i in range(2,n):
    if n%i ==0:
    
      flag=True
  
  if flag==False:
      cnt+=1
    
  N-=1
  
  
print(cnt)   
