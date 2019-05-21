def generate(s1,f1):
  for i in range(1,m):
    if f1==0:
      s1+='G'
      f1=1
    elif f1==1:
      s1+='R'
      f1=0
  return s1
n,m=map(int,input().split())
cherry=[]
for i in range(n):
  cherry.append(input())
ch1=[]
ch1.append(generate('R',0))
ch1.append(generate('G',1))
total_cost=0
for i in cherry:
  min=100000000
  for j in ch:
    ind=0
    cost=0
    while ind<m:
      if i[ind]!=j[ind]:
        if i[ind]=='R':
          cost+=5
        elif i[ind]=='G':
          cost+=3
      ind+=1
    if min>cost:
      min=cost
  total_cost+=min
print(total_cost)
