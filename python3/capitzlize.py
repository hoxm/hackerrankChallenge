s = input()
l = list(s)

last = ' '
for i in range(len(l)):
    if l[i].islower() and last == ' ':
        l[i] = l[i].upper()
    last = l[i]

print(''.join(l))

