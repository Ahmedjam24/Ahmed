st1=input()
flag1=0
for i in range(0,len(st1)-1):
  for j in range(i+1,len(st1)):
    if st1[i]<st1[j]:
      flag1=1
      print(st1[j:])
      break
  if flag1==1:
    break
else:
  print(st1)
