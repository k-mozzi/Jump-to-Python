dic = {'name': '이수', 'major': 'architecture'}
print(dic.keys())
print(dic.values())
print(dic.items(), '\n')

print("dic.get('name'):", dic.get('name'), '\n')
'''
'dic[]'과 차이가 없지만, 'dic[]'는 잘못된 키를 불러왔을 때 오류가 발생하는 반면,
'dic.get()'은 NONE을 출력한다.
'''
print("dic.get('book','Jane Eyre'):", dic.get('book', 'Jane Eyre'), '\n')
# key 값이 없을 때 미리 정해 둔 디폴트 값 출력

print("'name' in dic:", 'name' in dic)
print("'book' in dic:", 'book' in dic)
