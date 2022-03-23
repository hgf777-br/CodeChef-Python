for _ in range(int(input())):
    n, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.reverse()
    r = 0
    for i, h in enumerate(a):
        if x > h:
            r = len(a[i:])
            break
    print(r)