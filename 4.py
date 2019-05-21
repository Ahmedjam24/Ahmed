s13,s23=input().split()
s1=0
if len(s13)>len(s23):
  s13,s23=s23,s13
i=0
while i<len(s13):
  s1+=(ord(s23[i])-ord(s13[i]))
  i+=1
for i in range(i,len(s23)):
  s1+=ord(s23[i])-ord('a')+1
print(s1)
