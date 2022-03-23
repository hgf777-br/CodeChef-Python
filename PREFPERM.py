for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    f = 1
    per = []
    for y in a:
        p = [str(x) for x in range(f,y+1)]
        if len(p) > 1:
            p[0], p[-1] = p[-1], p[0]
        per.extend(p)
        f = y+1
    
    print(" ".join(per))
    