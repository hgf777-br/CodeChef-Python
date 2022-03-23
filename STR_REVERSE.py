for _ in range(int(input())):
    s = input()
    n = len(s)
    s_rev = s[::-1]
    j = n-1
    r = 0
    for i in range(n-1, -1, -1):
        if s_rev[i] == s[j]:
            j -= 1
        else:
            r += 1
    print(r)
