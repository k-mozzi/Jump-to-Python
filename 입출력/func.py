# 매개변수 = 함수에 입력으로 전달된 값을 받는 변수
# 인수 = 함수를 호출할 때 전달하는 입력값

def add(a, b):  # 일반적인 함수
    result = a + b
    return result


c = add(b=8, a=3)  # 매개변수 사용
x = add(3, 8)
print(c)
print(x)
print('\n')


def say():  # 입력값이 없는 함수
    return 'hi'


d = say()
print(d)
print('\n')


def plus(a, b):  # 결괏값(return)이 없는 함수
    print('%d, %d의 합은 %d입니다.' % (a, b, a+b))


print(plus(3, 4))
print('\n')


def add_many(*args):  # 여러 개의 입력값을 받는 함수
    result = 0
    for i in args:
        result += i
    return result


result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
print('\n')


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)
print('\n')


def print_kwargs(**kwargs):  # 키워드 파라미터 : 입력값을 딕셔너리 형태로 출력
    return kwargs


print(print_kwargs(a=1))
print(print_kwargs(name='이수', age=22))
print('\n')


def add_and_mul(a, b):
    return a+b, a*b


result = add_and_mul(3, 4)
print(result)
# 함수의 결괏값이 여러개일 땐 하나의 튜플값으로 출력됨
# return문을 만나는 순간 결괏값을 돌려준 후 함수를 빠져나가므로 return을 2개 설정할 수 없음


def say_nick(nick):
    if nick == '바보':
        return  # print문에 진입하기 전에 함수를 빠져나감
    print(f'나의 별명은 {nick}입니다.')
# 문자열 출력과 결괏값(반환값)은 다른 개념이다.


print(say_nick("갱"))
print(say_nick("바보"))
print('\n')


# 초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다.
# (name, old, man=True)는 가능하지만, (name, man=True, old)는 불가능!!
def say_myself(name, old, man=True):
    print(f'나의 이름은 {name}입니다.')
    print(f'나는 {old}살 입니다.')
    if man:
        return '나는 남자입니다.'
    else:
        return '나는 여자입니다.'


print(say_myself('김경모', 22, True))
print(say_myself('김용현', 22, False))
# True, False 부분을 기입하지 않으면 초깃값인 True로 출력
# 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다.
print('\n')


add = lambda a, b: a+b
result = add(3, 4)
print(result)
# lambda는 def와 동일한 역할을 함 : 함수를 생성할 때 사용하는 예약어
# lambda로 만든 함수는 return이 없어도 결괏값을 돌려준다.

''' 코드 정리 기능을 사용하자 lambda로 만든 코드가
def로 만든 코드로 바뀌는 것을 보니 lambda는 실무에서 자주
사용하는 방식이 아닌 것 같다.'''