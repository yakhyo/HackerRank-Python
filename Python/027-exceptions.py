if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = input().strip().split()
        try:
            print(int(a)//int(b))
        except Exception as e:
            print('Error Code:',e)