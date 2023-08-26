n = int(input())
arr = list(map(int, input().split()))

maxnum = max(arr)
maxindex = arr.index(maxnum)
chk = 1

for i in range(0, maxindex):
    if arr[i] <= arr[i+1]:
        chk = 1
    else:
        chk = 0
        break

for i in range(maxindex, n-1):
    if arr[i] >= arr[i+1]:
        chk = 1
    else:
        chk = 0
        break
if chk == 1:
    answer = sum(arr)
else:
    answer = 0

print(answer)
