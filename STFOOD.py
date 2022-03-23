T = int(input())
for tc in range(T):
    n = int(input())
    stores = []
    for st in range(n):
        stores.append([int(x) for x in input().split()])
    
    sales = 0
    for st in stores:
        tmp = (st[1] // (st[0] + 1)) * st[2]
        if sales < tmp:
            sales = tmp
            
    print(sales)