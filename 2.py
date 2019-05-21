x1,y1=input().split()
m1=len(x)
n1=len(y)
if ((n1>m1)or(n1==m1)):
    i=0
    while i<m1 and x1[i]==y1[i]:
        i+=1
    print(n1-i)
else:
    i=0
    while i<n1 and x1[i]==y1[i]:
        i+=1
    a1=x1[i:]
    b1=y1[i:]
    l1=list(a1)
    #print(l1)
    j=0
    for c1 in b1:
        if c1 in l1:
            j+=1
            l1.remove(c1)
    print(m1-i-j)
