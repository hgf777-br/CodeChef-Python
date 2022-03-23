T = 1
for tc in range(T):
    for n in range(2,100,2):
        o = list(range(1, n+1))
        l = o.copy()
        f = 0
        for i in range(n):
            a = [l[x] for x in range(0,n,2)]
            b = [l[x] for x in range(1, n, 2)]
            l = a + b
            if l==o:
                f = i+1
                break    
        print(n,f, n-f)