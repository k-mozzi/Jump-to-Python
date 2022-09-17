import re

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m, '\n')
# | 메타 문자는 or과 동일한 의미로 사용된다.


print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'), '\n')
# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.


print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'), '\n')
# $는 문자열의 끝과 매치함을 의미한다.


# \A는 문자열의 처음과 매치됨을 의미한다.
# re.MULTILINE 옵션을 사용할 경우 ^은 각 줄의 문자열의 처음과 매치되지만 \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.


# \Z는 문자열의 끝과 매치됨을 의미한다.
# re.MULTILINE 옵션을 사용할 경우 $ 메타 문자와는 달리 전체 문자열의 끝과 매치된다.


p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'), '\n')
# \b는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace 에 의해 구분된다.
# \b는 파이썬 리터럴 규칙에 의하면 백스페이스(BackSpace)를 의미하므로 기호 r을 반드시 붙여 주어야 한다.


p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
# \B 메타 문자는 whitespace 로 구분된 단어가 아닌 경우에만 매치된다.
