T = int(input())
for tc in range(T):
    n = int(input())
    s = [int(x) for x in input().split()]
    r = 0
    while(True):
        try:
            p = s.index(0)
        except ValueError:
            pass
        else:
            s = s[:p]
        
        if len(s) == 0:
            break
        
        n = min(s)
        r += len(s)*n
        s = [x - n for x in s]
    
    print(r)
    