def solve(full_name):
    # write your code here
    return ' '.join(i.capitalize() for i in full_name.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
