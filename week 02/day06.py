from itertools import combinations

N = int(input())
S = input()

P = set()

blank = [i for i in range(1, N)]
comb = list(combinations(blank, 2))

for f, s in comb:
	P.add(S[:f])
	P.add(S[f:s])
	P.add(S[s:])

P = sorted(list(P))

result = 0

for f, s in comb:
	temp = 0
	
	temp += P.index(S[:f]) + 1
	temp += P.index(S[f:s]) + 1
	temp += P.index(S[s:]) + 1
	
	result = max(result, temp)

print(result)