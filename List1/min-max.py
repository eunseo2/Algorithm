for t in range(int(input())):
    n=int(input())
    
    lst=list(map(int,input().split()))
    result = max(lst)- min(lst)
    print("#{} {}".format(t+1,result))


