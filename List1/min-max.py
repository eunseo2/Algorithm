for t in range(int(input())):
    n=int(input())
    
    lst=list(map(int,input().split()))

    if(len(lst)==n):
        result = max(lst)- min(lst)
        print("#{} {}".format(t+1,result))
    else :
        print("입력범위를 초과하였습니다.")
