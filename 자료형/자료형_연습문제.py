pin = ('881120-106824')
print('성별을 나타내는 숫자:', pin[7])

a = "a:b:c:d"
print('a:b:c:d'.replace(':', '#'))

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

t1 = (1, 2, 3)
t1 = t1 + (4,)
print(t1)

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s1 = set(a)
l1 = list(s1)
print(l1)

a = {'A': 90, 'B': 80, 'C': 70}
print(a['B'])
print(a.pop('B'))  # 값 반환 후 삭제
