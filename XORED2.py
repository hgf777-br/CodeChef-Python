
for i in range(10):
    for j in range(i,10):
        for k in range(j,10):
            x = i^j^k
            if x == 1:
                print(f"{i} XOR {j} XOR {k}= ", x)
        