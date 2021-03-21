if __name__ == '__main__':

    for i in range(int(input())):
        x, a, y, b = input(), set(input().split()), input(), set(input().split())
        print('True') if a.issubset(b) else print('False')
