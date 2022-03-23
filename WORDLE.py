for _ in range(int(input())):
    s = input()
    t = input()
    print("".join(['g' if x == y else 'b' for x,y in zip(s,t)]))