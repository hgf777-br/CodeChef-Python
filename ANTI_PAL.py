from collections import Counter

T = int(input())
for tc in range(T):
    n = int(input())
    s = input()
    if n % 2 != 0:
        print("NO")
    else:
        t = Counter(s)
        l = t.values()
        if max(l) > n / 2:
            print("NO")
        else:
            print("YES")
            ts = sorted(t.items(), key=lambda x: x[1], reverse=True)
            r = list("".join(x*y for x,y in ts))
            
            i, j = 0, n//2-1
            while(i<j):
                r[j], r[i] = r[i], r[j]
        
                i+=1
                j-=1
            print("".join(r))
        
        