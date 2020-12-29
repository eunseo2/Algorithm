a = int(input())
sum=0

for i in range(1,10000):
  if sum < a:
    sum+=i
  else:
    print(i-1)
    break
