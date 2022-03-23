T = int(input())
for tc in range(T):
    n = int(input())
    s = input()
    ga = 0
    gb = 0
    ca = n
    cb = n

    for i,st in enumerate(s):
        if i % 2 == 0:
            ga += int(st)
            ca -= 1
        else:
            gb += int(st)
            cb -= 1
        
        if ga > gb + cb or gb > ga + ca:
            print(i+1)
            break
    if ga == gb:
        print(2*n)
