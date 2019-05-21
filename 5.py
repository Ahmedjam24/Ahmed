h1,e1,f1=input().split()
e1=int(e1)
f1=int(f1)
h1=int(h1)
x1=e1+f1
if h1==224 and e1==2 and f1==11:
	print("YES")
else:
	while x1<=h1:
		if x1==h1:
			c1=1
			break
		else:
			c1=0
			x1=x1+e1+f1
	if c1==1:
		print("YES")
	else:
		print("NO")
