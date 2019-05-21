n1=int(input())
l1=[]
for i in range(0,n1):
	s1=input()
	l1.append(s)
c1=[]
for i in zip(*l1):
    if i.count(i[0])==len(i):
        c1.append(i[0])
    else:
        break
print(''.join(c1))
