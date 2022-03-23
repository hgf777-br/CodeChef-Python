TT = int(input())
for tc in range(T):
    x, y = [int(x) for x in input().split()]
    if x == 1:
        print(1)
    elif x == y:
        print(2*y - 1)
    else:    
        print(2*y + (x - y))