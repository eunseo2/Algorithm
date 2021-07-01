from itertools import combinations

def is_prime_number(x):
    for i in range(2,x):
        if x%i ==0 :
            return False
    return True

def solution(nums):
    answer = 0
    arr =list(combinations(nums,3))
    
    for n1,n2,n3 in arr:
        if is_prime_number(n1+n2+n3):
            answer +=1 
    
    return answer