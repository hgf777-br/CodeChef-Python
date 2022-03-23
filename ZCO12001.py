n = int(input())
s = [x for x in input().split()]
tmp = []
sub = []
d = 0
d_max = [0,0]
for i,c in enumerate(s):
    if c == '1':
        tmp.append(i)
        d += 1
    elif len(tmp) > 0 and c == '2':
        sub.append((tmp.pop()+1, i+1))
        d -= 1
    if d_max[0] < d:
        d_max = [d,i+1]

s_max = [0,0]    
for x in sub:
    t = x[1] - x[0] + 1
    if s_max[0] < t:
        s_max = [t, x[0]]

print(*d_max, *s_max)