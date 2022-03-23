n = 2
s = [1]

f = []
tmp = 0
m = 0
p = 0
i = 0
while i < (len(s)):
    if s[i] not in f:
        if len(f) < n - 1:
            f.append(s[i])
            tmp += 1
        else:
            tmp = 0
            j = p
            while(s[j] == f[0]):
                j += 1
            p = j
            i = j - 1
            f = []
    else:
        tmp += 1
    m = max(tmp, m)
    i += 1
        
print(m)