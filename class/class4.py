class FourCal:
    def __init__(self):
        self.first = 0
        self.second = 0

    def set_data(self, first, second):
        self.first = first
        self.second = second


a = FourCal()
b = FourCal()
a.set_data(4, 2)
b.set_data(3, 7)

print(id(a.first))  # 객체의 주소를 돌려주는 파이썬 내장 함수
print(id(b.first))  # 객체 변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다
