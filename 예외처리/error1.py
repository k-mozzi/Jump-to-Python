try:
    4 / 0
except:
    print('오류입니다.')
# 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행


try:
    4 / 0
except ZeroDivisionError:
    print('오류입니다.')
# 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행


try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
# 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법
