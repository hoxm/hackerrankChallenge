
import re

string = input()
sub_string = input()

count = 0
idx = 0

while True:
    if re.search(sub_string, string[idx:]):
        count = count + 1
        idx = idx + string[idx:].index(sub_string) + 1
    else:
        break

print(count)

