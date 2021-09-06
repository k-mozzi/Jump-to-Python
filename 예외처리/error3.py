try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱할 수 없습니다.')


try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
# 2개 이상의 오류를 동일하게 처리하기 위해서는 괄호를 사용한다.
