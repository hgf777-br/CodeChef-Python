T = int(input())
for tc in range(T):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    
    for i in range(n):
        for j in range(i+1,n):
            b.append(a[i] & a[j])
    
    while(len(b) > 1):
        b.sort()
        c = b.pop(0) | b.pop()
        b.append(c)        
    print(b[0])