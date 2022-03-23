T = int(input())
for tc in range(T):
    z,y,a,b,c = map(int, input().split())
    
    saldo = z - y
    custo = a + b + c
    if (saldo - custo ) >= 0:
        print("YES")
    else:
        print("NO")