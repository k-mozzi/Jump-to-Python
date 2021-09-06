import mod1
print(mod1.add(2, 5))
print(mod1.sub(8, 2))
#  import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.


from mod1 import add
print(add(3, 5))


from mod1 import add, sub


from mod1 import *
# * 문자는 '모든 것'이라는 뜻으로, 모든 함수를 불러 사용하겠다는 의미이다.
