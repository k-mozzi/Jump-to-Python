import re

p = re.compile('[a-z]+')

m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')
# match 의 결괏값이 있을 때만 그다음 작업을 수행하겠다는 의미
