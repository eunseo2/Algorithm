a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

c1= a2* b2
c2 = (a1*b2) + (a2*b1)

GCD=0

if c1>c2:
  a=c1
  b=c2
else:
  a=c2
  b=c1


while 1:
  r=a%b 
  if r==0 :
    GCD =b 
    break
  else:
    a=b 
    b=r 
    

if GCD!=0:
    c1=c1//GCD
    c2=c2//GCD
    
    
print(c2,c1)
