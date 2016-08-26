n = int(input())
list_all = input().strip().split()
set_all = set(list_all)
for i in set_all:
    try:
        list_all.remove(i)
        list_all.remove(i)
    except ValueError as e:
        print(i)
        break

