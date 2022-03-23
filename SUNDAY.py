for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    h = [6, 13, 20, 27, 7, 14, 21, 28]
    print(8 + len([x for x in a if x not in h]))
