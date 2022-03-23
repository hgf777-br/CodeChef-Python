for _ in range(int(input())):
    s = input()
    if len(s) < 3:
        print(-1)
    else:
        r = 0
        c = 1
        x = 1
        sub1 = []
        while x < len(s) - 1:
            i = 0
            if s[x] == s[i]:
                sub1.append(s[c:x])
                x += 1
                i += 1
                while s[x] == s[i] and x < len(s) - 1:
                    x += 1
                    i += 1
                c = x
            x += 1
        if x - c > 1:
            sub1.append(s[c:x+1])
        
        sub2 = []
        for sb in sub1:
            c = len(sb) - 1
            x = len(sb) - 1
            while x >= 0:
                i = len(s) - 1
                if sb[x] == s[i]:
                    l = len(sb[x+1:c+1])
                    if l > 0:
                        sub2.append(l)
                    x -= 1
                    i -= 1
                    while sb[x] == s[i] and x >= 0:
                        x -= 1
                        i -= 1
                    c = x
                x -= 1
            if c - x >= 1:
                sub2.append(len(sb[x+1:c+1]))
        
        r = -1 if len(sub2) == 0 else max(sub2)
        r = -1 if r == 0 else r
        print(r)
