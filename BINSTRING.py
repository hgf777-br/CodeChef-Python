for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 1
    for x in range(n-1):
        c += s[x] != s[x+1]
    print(c)
