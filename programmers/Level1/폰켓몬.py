def solution(nums):
    answer = 0
    choice = len(nums)//2
    
    temp = list(set(nums))
    
    for value in temp:
        if(answer < choice):
            answer +=1


    return answer