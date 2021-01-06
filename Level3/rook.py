c = [list(map(int,input().split())) for _ in range(8)]

rx=0
ry=0
king=0

for i in range(8):
  for j in range(8):
    if c[i][j]== 2:
      rx=i 
      ry=j
      for k in range(ry+1,8):
        if c[rx][k] ==1:
          king=1
        elif c[rx][k]==3:
          break
        
      for k in range(ry-1,-1,-1): 
        if c[rx][k] ==1:
          king=1
        elif c[rx][k]==3:
          break
      for k in range(rx+1,8):
        if c[k][ry] ==1:
          king=1 
        elif c[k][ry]==3:
          break
      
      for k in range(rx-1,-1,-1):
        if c[k][ry] ==1:
          king=1 
        elif c[k][ry]==3:
          break

print(king)
   

  
  
  
