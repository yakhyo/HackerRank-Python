def mutate_string(string, position, character):
    list_ = list(string)
    list_[position] = character

    return ''.join(list_)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)