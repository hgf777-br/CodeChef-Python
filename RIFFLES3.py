import math
import time

def is_power_two(n):
    return n and (not(n & (n-1)));

T = int(input())
for tc in range(T):
    n,k = [int(x) for x in input().split()]
    start = time.perf_counter()
    o = list(range(1, n+1))
    l = [[]]
    l[0] = o.copy()
    f = 0
    for i in range(n):
        a = [l[i][x] for x in range(0,n,2)]
        b = [l[i][x] for x in range(1, n, 2)]
        l.append(a + b)
        if l[-1]==o:
            f = i+1
            break
    k = k%f if f != 0 else k
    
    #print(*l[k])
    print(f)
    end = time.perf_counter()
    print(f"tempo gasto : ", end-start)
    