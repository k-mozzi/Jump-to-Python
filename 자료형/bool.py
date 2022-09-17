# 문자열, 리스트, 튜플, 딕셔너리의 값이 비어있으면(" ", [ ], ( ), { }) 거짓이다.
# 숫자의 경우 값이 0이면 거짓이다.


a = [1, 2, 3, 4]
while a:  # a가 거짓이 될 때까지 마지막 요소 출력
    print(a.pop())
    if []:  # []가 비어있으므로 '거짓' 출력
        print('참')
    else:
        print('거짓')

print('')
print(bool([1, 2, 3]))
print(bool(''))
print(bool(0))
