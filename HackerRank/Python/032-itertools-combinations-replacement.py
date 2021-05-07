from itertools import combinations_with_replacement

word, k = input().rstrip().split()

combinations = combinations_with_replacement(sorted(word), int(k))

for i in combinations:
    print(''.join(i))


