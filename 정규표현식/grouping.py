import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m, '\n')
# 그룹을 만들어 주는 메타 문자는 ( )이다.
# 특정 문자열이 계속해서 반복되는지 조사하거나
# 매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위해 사용한다.


p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('Kim 010-1234-5678')
print(m.group(2), '\n')
# group(0)	매치된 전체 문자열
# group(1)	첫 번째 그룹에 해당되는 문자열
# group(2)	두 번째 그룹에 해당되는 문자열
# group(n)	n 번째 그룹에 해당되는 문자열
# 그룹 중첩 사용 가능!


p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the rain')
print(m.group(), '\n')
# 그루핑된 문자열 재참조하기
# \1은 정규식의 그룹 중 첫 번째 그룹을 가리킨다.


p = re.compile(r'(?P<name>\w+)\s+(?P<num>\d+[-]\d+[-]\d+)')
m = p.search('Kim 010-1234-5678')
print(m.group('name'))
print(m.group('num'), '\n')
# 그룹에 이름을 지어 주려면 (?P<그룹명>...)과 같은 확장 구문을 사용해야 한다.


p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group(), '\n')
# 긍정형 전방 탐색(?=...) : ...에 해당되는 정규식과 매치되어야 하며
# 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방 탐색(?!...) : ...에 해당되는 정규식과 매치되지 않아야 하며
# 조건이 통과되어도 문자열이 소비되지 않는다.


p = re.compile('blue|white|red')
print(p.sub('color', 'blue socks and red shoes', count=2), '\n')
# sub 메서드의 첫 번째 매개변수는 "바꿀 문자열(replacement)"이 되고, 두 번째 매개변수는 "대상 문자열"이 된다.
# 세 번째 매개변수로 count 값을 넘기면 바꾸는 횟수를 제어할 수 있다.
# subn 역시 sub 와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있다.


p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub('\g<phone> \g<name>', 'Kim 010-1234-1234'))
# \g<그룹이름>을 사용하면 정규식의 문자열 순서를 바꿀 수 있다.
# 그룹이름 대신 참조 번호를 사용해도 같은 결과를 돌려준다.


# non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용되며,
# 가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.
