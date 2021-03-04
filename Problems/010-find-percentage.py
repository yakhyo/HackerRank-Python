if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))
    query_name = input()
    sum_ = 0
    for i in student_marks[query_name]:
        sum_ += i

    str_ = '{:.2f}'.format(sum_ / 3)
    print(str_)
