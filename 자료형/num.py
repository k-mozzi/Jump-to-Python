# int = 정수
print(-1)
print(0)
print(1)

# float = 실수
print(1.1)
print((2.3),'\n')

print('1+1', 1+1)
print('2-1', 2-1)
print('2*2', 2*2)
print('2**4', 2**4)
print('4/2', 4/2)
print('5%2', 5%2) # 나머지 반환
print('5//2', 5//2,'\n') # 몫 반환

a = divmod(5, 2)
print(a,'\n') # 나머지와 몫 반환
print(divmod(5,3))

import math # 수학 관련 연산 모듈
print('math.sqrt(4)', math.sqrt(4)) # 제곱근
print('math.pow(4,3)', math.pow(4,3),'\n') # 제곱

import random
print('random.random()', random.random())