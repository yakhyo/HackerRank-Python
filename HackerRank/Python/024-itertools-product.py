from itertools import product

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
print(*list(product(a, b)))
