class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

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


class MoreFourCal(FourCal):  
    def pow(self): # a의 b제곱을 구하는 함수
        result = self.first ** self.second
        return result


a = MoreFourCal(4, 2)
print(a.pow())