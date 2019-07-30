data = [0, 3, 1, 3, 1, 2, 4, 1]
counts = [0] * 5


for val in data:
    counts[val] += 1

print(counts)


sorted = []
for i in range(len(counts)):  #카운트 별에서 하나씩 값을 읽어옴
    for j in range(counts[i]):
        sorted.append(i)

print(sorted)


# 카운트 별에서 누적빈도수
for i in range(1, len(counts)):
    counts[i] = counts[i - 1] + counts[i]


# 연습문제 1
# 배열 활용 예제 : Gravity
data = [7, 4, 2, 0, 0, 6, 0, 7, 0] 



data = 'ABC'
n = len(data)
for i in range(n):
    for j in range(n):
        if i == j: continue
        for k in range(n):
            if i == k or j == k: continue
            print(data[i], data[j], data[k])

