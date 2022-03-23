T = int(input())
for tc in range(T):
    x = int(input())
    if x == 1:
        print("1 2 5")
    else:
        n = []
        for i in range(x):
            t = x ^ 2**i
            if  t != x:
                n.append(t)
            if len(n) == 2:
                break
        
        print(x,n[0], n[1])
    