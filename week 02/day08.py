N = int(input())

result = N // 14
N %= 14

result += N // 7
N %= 7

result += N

print(result)