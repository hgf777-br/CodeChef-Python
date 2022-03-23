s = "((A+B)*D)^(E-F)"
s = "A+(B*C-(D/E^F)*G)*H"
#s = "A+B*C-D/F"

def pre(c):
    d = {'^':3, '*':2, '/':2, '+':1, '-':1}
    return d.get(c,-1)

#for _ in range(int(input())):
#    n = int(input())
infix = s
stack = []
postfix = []

for c in infix:
    if c .isalpha():
        postfix.append(c)
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while len(stack) and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    else:
        while len(stack) and pre(stack[-1]) >= pre(c):
            postfix.append(stack.pop())
        stack.append(c)
    
while len(stack):
    postfix.append(stack.pop())

print("".join(postfix))