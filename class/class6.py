class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
# 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드이다.

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 2)
print(a.add())
# __init__ 메서드도 다른 메서드와 마찬가지로 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다.


class MoreFourCal(FourCal):  # 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 클래스가 상속된다.
    pass


b = MoreFourCal(4, 2)
print(b.add())
print(b.sub())
# 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황일 때 상속을 사용한다.
