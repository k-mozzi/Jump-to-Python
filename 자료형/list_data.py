a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][0], '\n')  # 리스트 안에 있는 리스트의 0번째 문자 출력

b = [1, 2, 3, 4, 5]
print(b[0:2])
print(b[1:4])
print(b[:2])
print(b[:5])
print(b[2:])
print(b[4:], '\n')

c = [1, 2, 3, 4]
d = [5, 6, 7, 8]
print(c + d, '\n')

# str 함수 : 정수 및 실수를 문자열의 형태로 만들어주는 함수
print(str(c[2]) + 'hi', '\n')

c[2] = 5  # 리스트 c의 2번째 값 수정
print(c[2])

del c[1]  # 리스트 c의 1번째 값 삭제
print(c)
del c[:2]
print(c)
