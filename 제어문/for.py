test_list = ['one', 'two', 'three']
for a in test_list:
    print(a)
print('\n')


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print(f'{number}번 학생은 합격입니다.')
    else:
        print(f'{number}번 학생은 불합격입니다.')
print('\n')


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue  # continue 나오면 print문은 공백 없이 작성
    print(f'{number}번 학생 축하합니다. 합격입니다.')
print('\n')


a = range(10)
print(a)
b = range(1, 11)  # 끝 숫자는 미포함
print(b, '\n')


add = 0
for i in range(1, 11):
    add = add + i

print(add, '\n')  # 1부터 11까지의 합 출력


marks = [90, 25, 67, 45, 80]
for num in range(len(marks)):
    if marks[num] < 60:
        continue
    print(f'{num+1}번 학생 축하합니다. 합격입니다.')
print('\n')


# 구구단 코드
for m in range(2, 10):
    for d in range(1, 10):
        print(m*d, end=' ')  # 다음 줄로 넘기지 않고 계속 출력하게 해줌
    print(" ")  # 두 번째 for문이 끝나면 줄 바꿈을 시켜줌
print('\n')


a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result, '\n')

# 리스트 내포
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result, '\n')

# [표현식 for 항목 in 반복가능객체 if 조건문]
a = [1, 2, 3, 4]
result = [num*3 for num in a if num % 2 == 0]
print(result)
