for _ in range(int(input())):
    #n = int(input())
    for n in range(1000,1101):
        l = list(range(1,n+1))
        r = 1
        while (len(l) > 1):
            t = l[0]
            c = 0
            a = t*2**c
            while (a <= n):
                l.remove(a)
                c += 1
                a = t*2**c
            r += 1

        print(n, r)
