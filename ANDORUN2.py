T = int(input())
for tc in range(T):
    s = int(input())
    a = [int(x) for x in input().split()]
    bits = [0]*30
    
    for n in a:
        idx = 0
        while (n > 0):
            bits[idx] += n & 1
            n = n >> 1
            idx += 1
    r = 0
    for idx, n in enumerate(bits):
        if n >= 2:
            r += 2**idx
    
    print(r)        
            
