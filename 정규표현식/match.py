import re

p = re.compile('[a-z]+')

m = p.match('python')

print(m)

n = p.match('3 python')

print(n)
# 문자열의 처음부터 정규식과 매치되는지 조사한다.
