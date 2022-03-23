for _ in range(int(input())):
    n = int(input())
    s = input()
    r = 1
    c = s[0]
    d = False
    for i in range(1,len(s)):
        if s[i] == c and not d:
            d = True
        else:
            r += 1
            d = False
        c = s[i]
    
    print(r)    
