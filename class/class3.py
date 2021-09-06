class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


a = FourCal()
a.setdata(4, 2)
# setdata 메서드의 첫 번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달된다.
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.

FourCal.setdata(a, 4, 2)
# 클래스 이름.메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 전달해 주어야 한다.
