for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(len([x for x in a if x >= 10 and x <= 60]))
