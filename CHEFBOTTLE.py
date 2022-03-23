for _ in range(int(input())):
    n, x, k = [int(x) for x in input().split()]
    q = n if k // x > n else k // x
    print(q)
