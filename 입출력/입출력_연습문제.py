def is_odd(num):
    if num % 2 == 0:
        return '짝수입니다.'
    else:
        return '홀수입니다.'


print(is_odd(4))
print('\n')


def mean(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)


print(mean(1, 2, 3, 4, 5))
print('\n')


input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
print('\n')


f1 = open("test.txt", 'w')
f1.write("Life is too short\n")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

f3 = open("test.txt", 'a')
f3.write('you need java')
f3.close()

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
