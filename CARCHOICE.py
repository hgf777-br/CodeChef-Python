for _ in range(int(input())):
    x1, x2, y1, y2 = [int(x) for x in input().split()]
    c1 = y1 / x1
    c2 = y2 / x2
    if c1 == c2:
        print(0)
    elif c1 < c2:
        print(-1)
    else:
        print(1)
