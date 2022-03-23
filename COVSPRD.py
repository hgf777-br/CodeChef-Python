T = int(input())
for tc in range(T):
    n,d = [int(x) for x in input().split()]

    if (d <= 10):
        si = 1*(2**d)
    else:
        si = 1024*(3**(d-10))
    print(si)
    print(n if si > n else si)    