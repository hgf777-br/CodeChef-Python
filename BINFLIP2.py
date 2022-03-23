T = 1
for t in range(T):
    S = [int(x) for x in "00010011010010101000101010010101110101010101010001001010101010100100101010101011110101010101011101010101101011011011101011"]
    run = True
    if "0" not in S and len(S) % 2 == 0:
        run = False
    size = len(S)
    op = []
    op_type = 0
    idx = 0
    while ((len(op)-1) <= size and sum(S) != 0 and run):
        run = False
        while (idx < size):
            if S[idx] == 0:
                idx += 1
                continue
            
            if op_type != 1 and idx + 3 <= size and sum(S[idx:idx+3]) == 2:
                if len(op) == 0:
                    op.append(1)
                op.append(idx)
                for i in range(3):
                    if S[idx+i] == 1:
                        S[idx+i] = 0
                    else:
                        S[idx+i] = 1
                op_type = 1
                run = True
                
            elif op_type != 2:
                if len(op) == 0:
                    op.append(2)
                S[idx] = 0
                op.append(idx)
                op_type = 2
                run = True
            
            elif op_type != 1 and idx + 3 <= size and sum(S[idx:idx+3]) == 1:
                op.append(idx)
                for i in range(3):
                    if S[idx+i] == 1:
                        S[idx+i] = 0
                    else:
                        S[idx+i] = 1
                op_type = 1
                run = True
                
            idx += 1
        idx = 0

    if sum(S) != 0:
        print("No")
    else:
        print("Yes")
        print(len(op)-1)
        for x in op:
            print(x)