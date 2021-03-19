if __name__ == '__main__':
    N = int(input())
    res = []
    for i in range(N):
        command, *numbers = input().split()

        numbers = list(map(int, numbers))

        if command == 'insert':
            res.insert(numbers[0], numbers[1])
        elif command == 'print':
            print(res)
        elif command == 'remove':
            res.remove(numbers[0])
        elif command == 'append':
            res.append(numbers[0])
        elif command == 'sort':
            res.sort()
        elif command == 'pop':
            res.pop()
        elif command == 'reverse':
            res.reverse()


