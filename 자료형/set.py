s1 = set('Hello')
s2 = set([1,2,3])
print('s1:', s1,'\n')
# 중복을 허용하지 않는다.
# 순서가 없다.

l1 = list(s2)
print('l1:', l1)
print('l1[1]:',l1[1],'\n')
# 인덱싱을 하기 위해선 집합을 리스트나 튜플 형태로 바꿔야 한다.

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print('s3 & s4:', s3 & s4) # 교집합
print('s3.intersection(s4):',s3.intersection(s4),'\n')

print('s3|s4:', s3|s4) # 합집합
print('s3.union(s4):', s3.union(s4),'\n') 

print('s3-s4:', s3-s4) #차집합
print('s3.difference(s4):', s3.difference(s4),'\n')

s3.add(7) # 요소 추가 (한 번에 2개 이상 추가는 불가)
print('s3:', s3,'\n')

s3.update([8,9]) # 2개 이상의 요소 추가
print('s3:', s3,'\n')

s3.remove(1) # 특정 값 제거 (한 번에 2개 이상 제거 불가)
print('s3:', s3)