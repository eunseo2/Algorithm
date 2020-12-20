for T in range(int(input())):
    N=int(input())
    
    n=list(map(int,input().split()))
    result = max(n)- min(n)
    print("#{} {}".format(T+1,result))


