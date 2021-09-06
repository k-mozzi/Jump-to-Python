# iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.


print(abs(3))
print(abs(-4))
print(abs(3.4))
print('\n')
# abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다.


print(all([1, 2, 3]))
print(all([1, 2, 4, 0]))
print(all([]))
print('\n')
# all(x)는 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
# all의 인수가 비어있을 땐 True를 돌려준다.


print(any([1, 2, 3]))
print(any([1, 2, 4, 0]))
print(any([0, '']))
print(any([]))
print('\n')
# any(x)는 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다.
# any의 인수가 비어있을 땐 False를 돌려준다.


print(chr(97))
print(chr(44032))
print('\n')
# chr(i)는 유니코드(Unicode) 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
print(ord('a'))
print(ord('가'))
print('\n')
# ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.


print(dir([1, 2, 3]))
print('\n')
print(dir({'1': 'a'}))
print('\n')
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.


print(divmod(7, 3))
print(divmod(8, 3))
print('\n')
# divmod(a, b)는 2개의 숫자를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.


for i, name in enumerate(['apple', 'lemon', 'melon']):
    print(i, name)
print('\n')
# enumerate는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
# enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.


print(eval('1 + 2'))
print(eval("'see' + 'you'"))
print(eval('divmod(8, 5)'))
print('\n')
# eval(expression)은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
# 코드가 길어지기만 하는데, 굳이 사용할 필요가 있나??


def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive([1, -3, 2, 0, -5, 6]))

# 양수만을 출력하는 코드를 filter를 이용하여 더욱 간단하게 만들면


def positive2(l):
    return l > 0


print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))
print('\n')
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
# 여러개의 값을 묶어서 반환하기 때문에 list를 사용하는 듯하다.


print(hex(123))
print(hex(203))
print('\n')
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
