number = input('숫자를 입력하세요: ')
print(number, '\n')
# input은 입력되는 모든 것을 문자열로 취급한다.


print('I''love''you')
print('I'+'love'+'you', '\n')
# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다.


print('I', 'love', 'you', '\n')
# 문자열 띄어쓰기는 콤마로 한다


for i in range(10):
    print(i, end=' ')
# 한 줄에 결괏값을 계속 이어서 출력하려면 end를 사용해 끝 문자를 지정해야 한다.
