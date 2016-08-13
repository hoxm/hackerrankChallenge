# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator as op

in_a = input()
in_b = input()

if in_a == '' or in_b == '':
    print('Fail to get two integers!')
else:
    operators = [op.add, op.sub, op.mul]
    a = int(in_a)
    b = int(in_b)

    for r in [ op_func(a, b) for op_func in operators ]:
        print(r)
