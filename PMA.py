for _ in range(int(input())):
    n = int(input())
    a = [abs(int(x)) for x in input().split()]
    print(a)
    l1 = sorted(a[::2])
    print(l1)
    l2 = sorted(a[1::2])
    print(l2)
    print('-'*30)
    s1 = sum(l1) - sum(l2)
    l1[0], l2[-1] = l2[-1], l1[0]
    print(l1)
    print(l2)
    s2 = sum(l1) - sum(l2)
    print(max(s1,s2))