cube = lambda x: x * x * x  # complete the lambda function


def fibonacci(n):
    fib = []
    f1, f2 = 0, 1
    for i in range(n):
        fib.append(f1)
        f1, f2 = f2, f1 + f2
    return fib

    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))