s = input()
l = len(s)

if l < 1:
    print('String is empty!')
elif l <= 500:
    print(s)
else:
    print('String is too long (>500)!')
