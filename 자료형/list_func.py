a = [1, 2, 3]  # 리스트에 요소 추가
a.append(4)
print(a, '\n')

b = [2, 1, 4, 3]  # 리스트 정렬
b.sort()
print(b, '\n')

c = ['c', 'a', 'b']
c.sort()
print(c, '\n')

d = [1, 2, 3]  # 리스트 뒤집기
d.reverse()
print(d, '\n')

e = ['a', 'b', 'c']  # 위치 반환
print(e.index('b'), '\n')

f = [2, 3, 4]  # n번째 위치에 문자 삽입
f.insert(0, 1)
print(f, '\n')

g = [1, 2, 3, 1, 2, 3]  # 리스트에서 첫번째로 나오는 x 삭제
g.remove(3)
print(g, '\n')

h = [1, 2, 3]  # 리스트의 n번째 위치 값을 반환한 후 해당 값 삭제
print(h.pop())
print(h)
print(h.pop(1))
print(h, '\n')

i = [1, 2, 3, 1, 1, 2, 3]  # x의 개수 세기
print(i.count(1))
