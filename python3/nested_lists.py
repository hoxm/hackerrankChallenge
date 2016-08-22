N = int(input())
students = []

for i in range(0, N):
    students.append([input(), float(input())])

# Get the second lowest score
scores = [ s[1] for s in students ]
scores.sort(reverse=True)
score_second = scores[scores.index(scores[-1]) - 1]

# Get sorted student names who's score is the second lowest score
students_second = [ s[0] for s in students if s[1] == score_second ]
students_second.sort()

for s in students_second:
    print(s)

