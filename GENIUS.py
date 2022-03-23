for _ in range(int(input())):
    n, x = [int(x) for x in input().split()]
    if n*3 < x:
        print("NO")
    else:
        c, d = divmod(x, 3)
        if d == 0:
            print("YES")
            print(c, 0, n-c)
        else:
            c += 1
            i = c * 3 - x
            if i > n - c:
                print("NO")
            else:
                print("YES")
                u = 0
                print(c,i,n-(c+i))
