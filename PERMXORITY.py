for _ in range(int(input())):
    n = int(input())
    m = [2, 3, 1]
    if n == 2:
        print(-1)
    elif n % 2 != 0:
        l = []
        for i in range(n, 0, -1):
            l.append(i)
        print(*l)
        m = l
    elif n == 4:
        print(3, 2, 4, 1)
    else:
        for i in range(4, n+1):
            m.append(i)
        print(*m)
    
    i = 1
    c = abs(m[0] - m[1]) 
    while i < len(m)-1:
        c = c ^ abs(m[i] - m[i+1])
        i += 1
    print(c)
