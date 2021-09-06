import statistics
print('''Hello
world''')

print('''
Hello
world
''')

print("'1'+'1'", '1'+'1')
print('Hello world '*100)
print(len('Hello world'*100))
print('Hello world'.replace('world', 'universe'))
print('pithon'.replace('i', 'y'), '\n')

grades = [1, 2, 3]
print(statistics.mean(grades))
# statistics는 import를 통해 선언해야 사용 가능한데, replace는 그렇지 않은 이유는?
# 모듈, 변수, 함수의 차이점?
