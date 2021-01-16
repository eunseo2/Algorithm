def printBinary(n) :
  if n==1:
    print(1,end='')
  elif n==0:
    print(0,end='')
    
  else:
    printBinary(n//2)
    print(n%2,end='')
  
  
  
N=int(input())
printBinary(N)
