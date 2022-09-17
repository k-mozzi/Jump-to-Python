import re

p = re.compile('[a-z]+')

m = p.match('python')
# 위 코드를 축약하여 m = re.match('[a-z]+', "python") 처럼 사용할 수도 있다.

print(m.group())
# 매치된 문자열을 돌려준다.
print(m.start())
# 매치된 문자열의 시작 위치를 돌려준다.
print(m.end())
# 매치된 문자열의 끝 위치를 돌려준다.
print(m.span())
# 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
