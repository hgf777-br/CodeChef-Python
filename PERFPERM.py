for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    p = [x for x in range(1,n+1)]
    if k == 1:
        for i in range(2,n+1):
            print(i,end=" ")
        print(1)
    elif k == (n-1):
        print(2,1,end=" ")
        for i in range(3,n+1):
            print(i,end=" ")
    else:
        for i in range(2,n-k+2):
            print(i,end=" ")
        print(1,end=" ")
        for i in range(n-k+2,n+1):
            print(i,end=" ")