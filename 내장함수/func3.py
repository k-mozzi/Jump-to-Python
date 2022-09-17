print(pow(2, 3))
print(pow(4, 2))
print('\n')
# pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.


print(list(range(5)))
print(list(range(1, 11)))
print(list(range(1, 6, 2)))
print('\n')
# range함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
# 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
# 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. (끝 숫자는 해당 범위에 포함 X)
# 세 번째 인수는 숫자 사이의 거리를 말한다.


print(round(2.3))
print(round(4.7))
print(round(2.357, 2))
print('\n')
# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
# round 함수의 두 번째 매개변수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)이다.


a = [4, 2, 5, 1]
print(sorted([3, 5, 1]))
print(sorted(['b', 'c', 'a']))
print(sorted('python'))
print(sorted(a))
print('\n')
# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
# sort 함수는 list에만 적용되는 함수이다.



print(str(3))
print(str('hi'))
print(str('hi'.upper()))
print('\n')
# str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.


print(sum([1, 2, 3]))
print(sum([4, 5, 6]))
print('\n')
# sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.


print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((4, 5, 6)))
print('\n')
# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
# 만약 튜플이 입력으로 들어오면 그대로 돌려준다.


print(type('haha'))
print(type([1, 2, 3]))
print(type({'name': '경모', 'age': '22'}))
print('\n')
# type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.


print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip('abc', 'def')))
# zip(iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
