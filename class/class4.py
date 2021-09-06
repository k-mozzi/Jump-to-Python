class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)


print(id(a.first)) # 객체의 주소를 돌려주는 파이썬 내장 함수
print(id(b.first))
# 객체 변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다