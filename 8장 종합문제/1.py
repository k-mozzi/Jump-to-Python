a = 'a:b:c:d'
b = a.split(':')
print('#'.join(b))


a = {'A': 90, 'B': 80}
try:
    print(a[C])
except:
    print(70)


A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0

for a in A:
    if a >= 50:
        result += a

print(result)


# a+b=c b+c=d d+e=f

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


for i in range(10):
    print(fib(i))


a = input('숫자를 입력하세요: ')
num = a.split(',')
result = 0
for n in num:
    result += int(n)


print(result)


a = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
for y in range(1, 10):
    print(a * y, end=' ')


f = open('abc.txt', 'w')
f.write('''
AAA
BBB
CCC
DDD
EEE
''')
f.close()

f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()


f = open('sample.txt', 'w')
f.write('''70
60
55
75
95
90
80
80
85
100''')
f.close()

f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

add = 0
average = 0
for line in lines:
    score = int(line)
    add += score
average = add / len(lines)

f = open('result.txt', 'w')
f.write(str(average))
f.close()
# 숫자 값은 result.txt 파일에 바로 쓸 수 없으므로 str 함수를 사용하여 문자열로 변경한 후 파일에 쓴다.
