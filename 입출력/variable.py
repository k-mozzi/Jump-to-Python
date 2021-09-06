from copy import copy


name = ['경모', '용현', '동원']
message = 'Hi,' + name[2] + ', ' + name[1] + ' nice to meet you.'
print(message, '\n')


a = [1, 2, 3]
b = a
print(a is b)
a[1] = 4
print(b, '\n')
# a와 b는 동일하며, a의 값이 변화되면 b의 값도 바뀐다.
# 즉 a와 b의 메모리 상 주소는 같다.

c = [1, 2, 3]
d = c[:]  # c의 리스트를 복사
c[1] = 4
print(c)
print(d, '\n')  # c의 리스트 값을 변경해도 d에 영향을 끼치지 않는다.

e = [1, 2, 3]
f = copy(e)  # 'f = e(:)'와 같은 의미
print(e)
print(f)
print(e is f)  # c와 d가 같은 값을 갖지만, 가라키는 객체가 서로 다르다.
