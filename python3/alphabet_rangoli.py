from string import ascii_lowercase as lowers

N = int(input())
uses = lowers[:N]

for idx in range(-N+1, N):
    i = abs(idx)
    print(('-'.join(list(uses[-1:-(N-i):-1] + uses[i:]))).center(4*N-3, '-'))
