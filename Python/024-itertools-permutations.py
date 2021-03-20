from itertools import permutations

str_, k = input().split()

for i in sorted(list(permutations(str_, int(k)))):
    print(''.join(i))