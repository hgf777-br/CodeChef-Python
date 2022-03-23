from functools import reduce

def lista(p,n,x):
    if p == n:
        r = reduce(lambda x,y:x^y, l)
        if r == x:
            return True
        else:
            return False
    for i in range(10):
        if i in l:
            continue
        l[p] = i    
        r = lista(p+1,n,x)
        if r :
            return True

T = int(input())
for tc in range(T):
    n,x = [int(x) for x in input().split()]
    r = False
    l = [0]*n
    for i in range(1,10):
        l[0] = i
        r = lista(1,n,x)
        if r:
            break;
    print(l)