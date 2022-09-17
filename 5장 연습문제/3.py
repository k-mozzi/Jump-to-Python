def positive(l):
    return l > 0


print(list(filter(positive, [1, -2, 3, -5, 8, -3])))

print(int('0xea', 16))


def threetimes(a):
    return a * 3


print(list(map(threetimes, [1, 2, 3, 4])))

a = [-8, 2, 7, 5, -3, 5, 0, 1]
b = max(a)
c = min(a)

print(b + c)

print(round(5.666666666666667, 4))
