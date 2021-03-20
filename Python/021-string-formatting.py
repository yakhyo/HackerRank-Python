def print_formatted(number):
    # your code goes here
    len_ = len('{0:b}'.format(number))
    for i in range(1, number + 1):
        str_ = '{0:{len_}d} {0:{len_}o} {0:{len_}X} {0:{len_}b}'.format(i, len_=len_)
        print(str_)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
