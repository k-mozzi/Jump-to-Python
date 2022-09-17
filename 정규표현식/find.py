import re

p = re.compile('[a-z]+')

result = p.findall('life is too short')

print(result)
# split 함수와 비슷한 기능?
# 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.

result2 = p.finditer('life is too short')

print(result2)

for r in result2:
    print(r)
# 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
