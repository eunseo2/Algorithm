N=input()

cnt=0

if len(N)==1:
  print(N)

for i in range(0,len(N)-1):

  if N[i]==N[i+1]:

    cnt+=1
    
    if i== len(N)-2:
      print(cnt+1,end='')
      print(N[i],end='')
    
    

  else:
   
    if i== len(N)-2 and cnt==0:
      print(N[i],end='')
      print(N[i+1],end='')
      break
      
    if i==len(N)-2 and cnt>=1:
      print(cnt+1,end='')
      print(N[i],end='')
      print(N[i+1],end='')
      
    else:
     
      if cnt==0:
        print(N[i],end='')
      else:
        print(cnt+1,end='')
        print(N[i],end='')
        cnt=0
