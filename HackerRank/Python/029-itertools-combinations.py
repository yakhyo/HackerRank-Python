from itertools import combinations
text, k = input().strip().split()

for i in range(1, int(k)+1):
    for j in combinations(sorted(text), i):
        print(''.join(j))