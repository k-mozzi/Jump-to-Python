import re

p = re.compile('a.b')
m = p.match('a\nb')
print(m, '\n')

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m, '\n')
# DOTALL(S) - '.' 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# 옵션을 사용할 때는 re.DOTALL 처럼 전체 옵션 이름을 써도 되고 re.S 처럼 약어를 써도 된다.


p = re.compile('[a-z]+', re.IGNORECASE)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'), '\n')
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.


p = re.compile('^python\s\w+')

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))


p = re.compile('^python\s\w+', re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data),'\n')
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# ^는 문자열의 처음을 의미하고, $는 문자열의 마지막을 의미한다.


char = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
# 따옴표 앞 r은 백슬래시를 특수문자로 출력시켜준다.
