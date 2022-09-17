import re

p = re.compile('[a-z]+')

m = p.search('3 python')

print(m)
# match 는 문자열의 처음부터 검색하므로 None 을 출력하지만,
# search 는 문자열의 전체를 검색하므로 3 이후의 python 문자열과 매치된다.
