# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result = 0
a = 1
while a <= 1000:
    if a % 3 == 0:
        result += a
    a += 1

print(result,'\n')


a = 1
result = ''
while a < 6:
    a += 1
    result += '*'
    print(result,'\n')


for a in range(1,101):
    print(a, end=' ')
print('\n')


marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for mark in marks:
    result += mark

print(result / len(marks))
print('\n')


numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
# 홀수일 때만 2를 곱해서 출력하라

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)