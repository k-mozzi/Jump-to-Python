a = 'hobby'  # 문자 개수 세기
print(a.count('b'), '\n')

b = 'Python is the best choice'  # 위치 알려주기
print(b.find('b'))
print(b.find('k'), '\n')  # -1은 찾는 값이 없음을 의미

c = 'Life is too short'  # 위치 알려주기 2
print(c.index('t'))
print(c.index('i'), '\n')  # 찾는 값이 없으면 오류 발생

print("/".join('abcd'), '\n')  # 문자열 삽입

d = 'hi'  # 소문자를 대문자로 바꾸기
print(d.upper())
e = 'HI'  # 대문자를 소문자로 바꾸기
print(e.lower(), '\n')

f = ' hi '
print(f.rstrip())  # 오른쪽 공백 지우기
print(f.lstrip())  # 왼쪽 공백 지우기
print(f.strip(), '\n')  # 양쪽 공백 지우기

g = 'Life is short'  # 문자열 바꾸기
print(g.replace('Life', 'Your leg'), '\n')

h = 'I like apple'  # 문자열 나누기
print(h.split())
i = 'a:b:c:d'
print(i.split(':'))
