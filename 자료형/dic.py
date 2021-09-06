dic = {'name': '이수', 'major': 'architecture'}

a = {1: 'a'}
a[2] = 'b'  # 딕셔너리 쌍 추가
print('a', a, '\n')
a['name'] = '이수'
print('a', a, '\n')

del a[1]  # 딕셔너리 요소 삭제
print('a', a, '\n')

print(dic['name'])
print(dic['major'])
# 딕셔너리에선 인덱싱을 적용할 수 없고 key를 통해 값을 반환받아야 한다.
# key가 중복되었을 땐 1개를 제외한 나머지 값은 무시된다.
# key에는 변하는 값이 올 수 없다. (ex : 리스트)
