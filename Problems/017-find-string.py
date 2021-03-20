def count_substring(string, sub_string):
    sub_length = len(sub_string)
    str_length = len(string)
    count = 0
    for i in range(0, str_length):
        if str_length - i < sub_length:
            break
        elif string[i:i + sub_length] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
