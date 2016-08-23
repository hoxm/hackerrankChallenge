
S = input().strip()
L = len(S)

vowels = 'AEIOU'
score_vowels = 0
score_consonants = 0

for i in range(L):
    # total sub strings which begin at this index
    # As start position is fixed, only count each possibility of length.
    total = L - i
    if S[i] in vowels:
        score_vowels = score_vowels + total
    else:
        score_consonants = score_consonants + total

if score_consonants > score_vowels:
    print('Stuart %d' % score_consonants)
elif score_consonants < score_vowels:
    print('Kevin %d' % score_vowels)
else:
    print('Draw')

