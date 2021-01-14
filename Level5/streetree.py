N=int(input())


lst=[]

for i in range (N):
  lst.append(int(input()))
 
arr=[]


for i in range(0,len(lst)-1):
    arr.append(int(lst[i+1])-int(lst[i]))
     

def GCDofTwoNumbers(a,b):
  while b !=0:
    a,b=b,a%b 
  return a 

GCDarr = arr[0]
for i in range(len(arr)):
  GCDarr=GCDofTwoNumbers(GCDarr,arr[i])



sum= int(max(lst))-int(min(lst))
sum/=GCDarr

cnt=sum-len(lst)+1
print(int(cnt))
  
