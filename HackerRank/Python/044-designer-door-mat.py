N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.'*i).center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(1, N, 2):
    print(('.|.'*(N-i-1)).center(M, '-'))