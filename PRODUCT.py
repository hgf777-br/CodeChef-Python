import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

for _ in range(int(input())):
    b,c = [int(x) for x in input().split()]
    print(lcm(b, c) // b)