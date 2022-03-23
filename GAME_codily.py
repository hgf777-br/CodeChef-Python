import re

def fragments(S):
    i = 0
    while i < len(S):
        d = 1
        while i+d < len(S) and S[i+d] == S[i]:
            d += 1
        if S[i] != '?':
            yield (i,d)
        i += d    

def solution(S):
    S = list(S)
    ans = 1
    for i, d in fragments(S):
        ans = max(ans, d)
        
    for i, d in fragments(S):
        if d == ans:
            other = 'a' if S[i] == 'b' else 'b'
            if i+d < len(S) and S[i+d] == '?':
                S[i+d] = other
            
    for i, d in fragments(S):
        ans = max(ans, d)
        
    return ans    
    
S = "??b??"
print(Solution(S))    