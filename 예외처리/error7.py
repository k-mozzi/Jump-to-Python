class MyError(Exception):
    def __str__(self):
        return '허용되지 않은 별명입니다.'
# __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
# 오류 클래스에만 적용되는 것인가?

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    else:
        return nick


print(say_nick('천사'))
print(say_nick('바보'))


try:
    print(say_nick('천사'))
    print(say_nick('바보'))
except MyError:
    print('허용되지 않은 별명입니다.')
