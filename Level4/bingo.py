def check():
  cnt=0
  
  for i in range(5):
    cnt_row=0
    cnt_col=0
    for j in range(5):
      if bingo[i][j]==0: cnt_col+=1
      if bingo[j][i]==0: cnt_row+=1
    
    if cnt_row==5: cnt+=1
    if cnt_col==5: cnt+=1
  
  cnt_l=0
  cnt_r=0
  
  for i in range(5):
    if bingo[i][i]==0:cnt_l +=1
    if bingo[i][5-1-i]==0: cnt_r +=1 
  if cnt_l == 5: cnt+=1 
  if cnt_r == 5 : cnt+=1 
  
  if cnt>=3: return True
  return False



bingo= [list(map(int,input().split())) for _ in range(5)]
a= [list(map(int,input().split())) for _ in range(5)]
b=sum(a,[])

cnt=0 

for k in b:
  for i in range(5):
    for j in range(5):
      if bingo[i][j]==k:
         bingo[i][j]=0
         cnt+=1
         if check() == True:
            print(cnt)
            exit()
