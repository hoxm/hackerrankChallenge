import re

number = input()

print(bool(re.match('^M{0,3}(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$', number)))

