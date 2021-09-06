money = 10000
card = True
if money > 2000 and card:
    print('택시를 타라' '\n')
else:
    print('버스를 타라' '\n')


if money < 2000 or card:
    print('택시를 타라' '\n')
else:
    print('버스를 타라' '\n')


if not card:
    print('택시를 타라' '\n')
else:
    print('버스를 타라' '\n')


print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('y' not in ('python'), '\n')


pocket = ['wallet', 'card', 'money']
if 'card' in pocket:
    print('택시를 타라' '\n')
else:
    print('버스를 타라' '\n')


if 'card' in pocket:
    pass  # 아무 것도 출력하지 않음
else:
    print('버스를 타라' '\n')


pocket1 = ['paper', 'wallet']
card = False
if 'money' in pocket1:
    print('택시를 타라' '\n')
elif card:  # 조건문이 거짓일 때 수행 (개수 제한 X)
    print('택시를 타라' '\n')
else:
    print('걸어가라' '\n')


score = 70
if score >= 60:
    messege = 'success'
    print(messege, '\n')
else:
    message = 'failure'
    print(message, '\n')

# 한 줄로 표시하면? = 조건부 표현식
# (조건문이 참인 경우) if (조건문) else (조건문이 거짓인 경우)
message = 'success' if score >= 60 else 'failure'
print(message)
