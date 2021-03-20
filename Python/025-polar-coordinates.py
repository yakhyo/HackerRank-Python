import cmath

complex_num = input()
print('{:.3f}'.format(abs(complex(complex_num))))
print('{:.3f}'.format(cmath.phase(complex(complex_num))))
