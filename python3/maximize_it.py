import itertools

L = []
max_sum = 0

K, M = list(map(int, input().strip().split()))
for i in range(K):
    L.append([int(n)**2 for n in input().strip().split()[1:]])

for i in itertools.product(*L):
    max_sum = max(max_sum, sum(i)%M)

print(max_sum)

