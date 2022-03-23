for _ in range(int(input())):
    s = input()
    if len(s) < 3:
        print(-1)
    else:
        sub = []
        x = c = 1
        while x < len(s) - 1:
            if s[x] in [s[0], s[-1]]:
                sub.append(len(s[c:x]))
                x += 1
                c = x
            else:
                x += 1
        if x - c > 0:
            sub.append(len(s[c:x]))
        r = 0 if len(sub) == 0 else max(sub)
        r = -1 if r == 0 else r
        print(r)
