class Bird:
    def fly(self):
        raise NotImplementedError
# NotImplementedError는 파이썬 내장 오류로,
# 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.

class Eagle(Bird):
    pass
# fly 함수가 부모 클래스에서 정의되지 않았으므로
# 오버라이딩이 필요한 상태

eagle = Eagle()
print(eagle.fly())
# 오류 발생