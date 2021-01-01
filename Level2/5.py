n,s = map(int,input().split())

s=s-1

for i in range(n):
    a=2*i+1
    s=s+a-1
    print(' '*(n-i-1),end="")
  
    for j in range(2*i+1):
        if i%2!=0:
            print(s%9+1,end='')
            s+=1
            
        else:
            print(s%9+1,end='')
            s-=1
    print()
