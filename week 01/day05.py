def count(num):
    b = bin(num)[2:]  # 2진수 변환 후 '0b' 접두사 제거
    cnt = 0

    for i in b:
        if i == '1':
            cnt += 1

    return cnt

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

# 1의 개수와 원래의 10진수를 함께 저장하는 리스트 생성
countNum = [(count(num), num) for num in numbers]

# 1의 개수를 기준으로 내림차순 정렬, 같은 경우 원래의 10진수를 기준으로 내림차순 정렬
result = sorted(countNum, key= lambda x: (x[0], x[1]), reverse=True)

answer = result[K-1][1]
print(answer)
