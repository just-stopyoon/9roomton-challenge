def play(sy, sx, N):
	y, x = sy, sx
	visited = [[0] * N for _ in range(N)]
	visited[y][x] = 1
	
	notEnd = True
	
	while notEnd:
		cnt = count[y][x]
		dy, dx = command[y][x]
		
		for _ in range(cnt):
			y = (y + dy) % N
			x = (x + dx) % N
			
			if visited[y][x]:
				notEnd = False
				break
			visited[y][x] = 1
	
	return sum([sum(i) for i in visited])

N = int(input())
Rg, Cg = map(int, input().split())
Rp, Cp = map(int, input().split())

Rg -= 1
Cg -= 1
Rp -= 1
Cp -= 1

arr = [list(input().split()) for _ in range(N)]

count = [[0] * N for _ in range(N)]
command = [[None] * N for _ in range(N)]
direction = {"L" : [0, -1], "R" : [0, 1], "U" : [-1, 0], "D" : [1, 0]}

for i in range(N):
	for j in range(N):
		temp = arr[i][j]
		count[i][j] = int(temp[:-1])
		key = temp[-1]
		command[i][j] = direction[key]

scoreG = play(Rg, Cg, N)
scoreP = play(Rp, Cp, N)

if scoreG > scoreP:
	print("goorm", scoreG)
else:
	print("player", scoreP)