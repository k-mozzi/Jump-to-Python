result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print(result)
# 15는 3과 5의 공배수이므로 둘 다 포함시키지 않기 위해
# or 연산자를 사용했다.
