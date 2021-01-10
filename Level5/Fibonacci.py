n= int(input())

lst=[0]*(n+1)

for i in range(n+1):
  if i==0 :
    lst[0]=0
    
  elif i==1 :
    lst[1]=1
    
  
  else :
    lst[i]= lst[i-1]+lst[i-2]
    
    
print(lst[n])
