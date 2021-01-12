n,m= map(int,input().split())


cntTwo=0
cntFive=0
cnttwo=0
cntfive=0

for i in range(n,n-m,-1):

  while i%2==0:
    i/= 2
    cntTwo+=1
    
  while i%5==0:
    i/=5
    cntFive+=1 


for j in range(m,0,-1):
  
  while j%2==0:
    j/= 2
    cnttwo+=1
    
  while j%5==0:
    j/=5
    cntfive+=1 
   
cntTwo=cntTwo-cnttwo
cntFive=cntFive-cntfive


if cntTwo > cntFive :
  print(cntFive)
else:
  print(cntTwo)
