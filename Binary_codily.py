def solution(N):
    b = f"{N:b}"
    print(b)
    ans = 0
    c = 0
    i = 0
    while (i < len(b)):
        if (b[i] == '1'):
            i += 1
            while (i < len(b) and b[i] == '0'):
                c += 1
                i += 1
            if (i < len(b) and b[i] == '1'):
                ans = max(ans, c)
                c = 0
        else:        
            i += 1        
        
    return ans            
n = 328
print(solution(n))    