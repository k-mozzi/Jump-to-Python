a = 3
b = a
print(id(3))
print(id(a))
print(id(b))
print('\n')
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.


a = int(input('숫자를 입력하세요: '))

if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
print('\n')
# input([prompt])은 사용자 입력을 받는 함수이다.


print(int('3'))
print(int(3.2))
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수이다.
print(int('11', 2))
print(int('1A', 16))
print('\n')
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.


class Person:
    pass


a = Person()
b = 3
print(isinstance(a, Person))
print(isinstance(b, Person))
print('\n')
# isinstance(object, class )는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.


print(len('123'))
print(len('hello'))
print('\n')
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.


print(list('Python'))
print(list((1, 2, 3)))
print('\n')
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
# list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.


def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)


# 결괏값의 2배를 출력하는 코드를 map을 사용하며 간단하게 만들면


def twotimes(x):
    return x * 2


print(list(map(twotimes, [1, 2, 3, 4])))
print('\n')
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.


print(max([1, 2, 3]))
print(max('python'))
print('\n')
# max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.


print(min([1, 2, 3]))
print(min('python'))
print('\n')
# min(iterable)은 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.


print(oct(8))
print(oct(13))
print('\n')
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
print(int('0o10', 8))
print(int('0o15', 8))
print('\n')
# 앞서 배운 int는 각 진수로 표현된 숫자를 10진수로 돌려주는 함수이다.


# open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다.
# 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
