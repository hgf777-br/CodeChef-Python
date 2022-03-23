def f(a,i,j):
    if i==j:
        return 1;
    s = set(a[i:j+1])
    return len(s)      


n,nq = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

s = []
for i in range(0,n):
    for j in range(i,n):
        s.append(f(a,i,j))
print(s)

for tc in range(nq):
    l = [int(x) for x in input().split()]    
    r1 = 0
    r2 = 0
    if (len(l)) == 2:
        q,k = l
        for i in range(k):
            for j in range(i,k):
                r1 += f(a,i,j)
        for i in range(k):
            r2 += s[i]
        print(r1,r2)        
    else:
        q,x,y = l
        a[x-1] = y