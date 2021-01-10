
a,b = map(int,input().split())

A=a 
B=b 
GCD=0

while 1:
  r=a%b 
  if r==0 :
    GCD =b 
    break
  else:
    a=b 
    b=r 
    

print((A//GCD)*(B//GCD)*GCD)
