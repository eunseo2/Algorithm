lst =[]

for i in range(0,3):
  a=input()
  if a.count("0")==0:
    lst.append("E")
  elif a.count("0")==1:
    lst.append("A")
  elif a.count("0")==2:
    lst.append("B")
  elif a.count("0")==3:
    lst.append("C")
  else:
    lst.append("D")
for i in lst:
  print(i)
