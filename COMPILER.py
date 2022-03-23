T = int(input())
for tc in range(T):
    s = input()
    sub = 0
    r = 0
    for i,c in enumerate(s):
        if c == '<':
            sub += 1
        elif c == '>':
            sub -= 1
            if sub < 0:
                break
        if sub == 0:
            r = i + 1

    print(r)
