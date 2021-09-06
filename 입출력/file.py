f = open('file.txt', 'w')
f.close
# f.close는 열려 있는 파일 객체를 닫아 주는 역할(작업 종료)을 한다.
# 파일 경로에 역슬래시(\)를 사용할 땐 역슬래시를 두 개 사용하거나,
# 문자열 앞에 r을 적어 줄바꿈 문자로 해석되지 않게 해야 한다.
'''
open 함수를 통해 파일 생성 : 파일 객체 = open(파일 이름, 파일 열기 모드)

r(읽기모드) : 파일을 읽기만 할 때 사용
w(쓰기모드) : 파일에 내용을 쓸 때 사용
a(추가모드) : 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
'''

f = open('newfile.txt', 'w')
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()


f = open('c:/Users/김경모/Desktop/python/newfile.txt', 'r')
line = f.readline()  # 파일을 한 줄씩 읽는 함수
print(line)
f.close()
print('\n')


f = open('c:/Users/김경모/Desktop/python/newfile.txt', 'r')
while True:  # readline 함수로 파일의 모든 줄을 읽는 경우
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
print('\n')


f = open('c:/Users/김경모/Desktop/python/newfile.txt', 'r')
lines = f.readlines()  # 파일의 모든 줄을 읽는 함수
for line in lines:
    line = line.strip()  # 공백 제거
    print(line)
f.close()
print('\n')
# readline과 readlines 헷갈리지 않기!


f = open('c:/Users/김경모/Desktop/python/newfile.txt', 'r')
data = f.read()  # 파일의 내용 전체를 문자열로 돌려주는 함수
data = data.strip()
print(data)
f.close()
print('\n')


f = open('c:/Users/김경모/Desktop/python/newfile.txt', 'a')
for a in range(11, 21):
    data = (f'{a}번째 줄입니다.\n')
    f.write(data)
f.close()
# 쓰기모드(w)로 파일을 열면 기존의 있던 내용이 삭제되므로,
# 추가모드(a)로 파일을 열어 내용을 작성한다.


with open('new.txt', 'w') as f:
    f.write('파이썬 공부 어렵다.')
with open('c:/Users/김경모/Desktop/python/new.txt', 'r') as f:
    data = f.read()
    print(data)
# with문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.
