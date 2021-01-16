def Factorial(x) :
  if x==0 :
    return 1
  else:
    return x * Factorial(x-1)
    
    
x=int(input())
print(Factorial(x))
