arr = [[10]*9 for _ in range(9)]

b=[]
for i in range(0,5):
  b.append(list(map(int,input().split())))
  

for i  in range(5):
  for j in range(5):
    arr[i+1][j+1] = b[i][j]



for i in range(1,6):
  for j in range(1,6):
    if arr[i-1][j] > arr[i][j] and arr[i][j-1] > arr[i][j] and arr[i+1][j] > arr[i][j] and arr[i][j+1] > arr[i][j] :
           print('*', end=' ')
    else:
      print(arr[i][j], end=' ')
       
  print()
