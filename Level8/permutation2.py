import itertools
n,r=map(int,input().split())

arr=[0]*n
for i in range(n):
  arr[i]= chr(i+ord('a'))

d=list(map(''.join, itertools.permutations(arr, r)))

for i in d:
  print(i)
