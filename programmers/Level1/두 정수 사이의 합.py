def solution(a, b):
    answer = 0
    for value in range(min(a,b), max(a,b)+1):
        answer += value
            
    return answer