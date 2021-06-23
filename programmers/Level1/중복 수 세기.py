# arr = [1,1,3,3,2,3,3,3,4,4]
# # arr = [1,2,3,4]

# def solution(arr):
#   check = []
#   result = []

#   for j in arr: 
#     if 1 < arr.count(j) and j not in check:
#       check.append(j)

#   for i in check:
#     result.append(arr.count(i))

#   if check == []:
#     return [-1]
#   else:
#     return result


# print(solution(arr)) 

def solution(a):
  temp = dict()
  answer =[]
  for i in a:
    if temp.get(i):
      temp[i] +=1 
    else:
      temp[i] = 1 
  for k,v in temp.items():
    if 1 !=v:
      answer.append(v)
  return -1 if len(answer) ==0 else answer

print(solution([3,3,2,2,2,1,1,1,1]))