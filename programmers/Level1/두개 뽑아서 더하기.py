from itertools import combinations

def solution(numbers):
    sum = list(combinations(numbers,2))
    answer = set()
    for num1,num2 in sum :
        answer.add(num1+num2)

    return sorted(answer)