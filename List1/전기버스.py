TC = int(input())
for tc in range(1, TC+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split())) + [N+K, N+K]
    #N 종점 K 이동가능 M 정류장 개수
    here = 0 #내위치
    i = 0 #정류장위치
    cnt = 0 #기름 넣을때 마다 +1
    while here + K < N :
       if here+K >=  data[i+2]:
           here = data[i + 2]
           cnt += 1
           i += 3
           continue
 
       elif here+K >=  data[i+1]:
           here = data[i + 1]
           cnt += 1
           i += 2
           continue
       elif here+K < data[i]:
           cnt = 0
           break
 
       else:
           here = data[i]
           cnt += 1
           i += 1
 
    print("#%d %d"%(tc, cnt))
