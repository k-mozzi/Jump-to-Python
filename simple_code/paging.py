def paging(a, b):
    if a % b == 0 or a % b < 0:
        return a // b
    else:
        return a // b + 1


print(paging(2, 6))
