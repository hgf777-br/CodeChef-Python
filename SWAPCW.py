for _ in range(int(input())):
    n = int(input())
    s = input()
    m = n // 2
    if n < 3:
        print('YES')
    elif n % 2 and ((s[m-1] < s[m] > s[m+1]) or (s[m-1] > s[m] < s[m+1])):
            print('NO')
    else:
        l = [x for x in s]
        r = 'YES'
        for i in range(m):
            if l[i] > l[n-1-i]:
                l[i], l[n-1-i] = l[n-1-i], l[i]
                if l[i] > l[i+1] or l[n-2-i] > l[n-1-i]:
                    r = 'NO'
                    break
        for i in range(m,n-1):
            if l[i] > l[i+1]:
                r = 'NO'
                break
        print(r,l)