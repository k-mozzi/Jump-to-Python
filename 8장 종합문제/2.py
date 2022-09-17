class Calculator:
    def __init__(self, first, second, third, fourth, fifth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth

    def sum(self):
        result = self.first + self.second + self.third + self.fourth + self.fifth
        return result

    def avg(self):
        total = self.sum()
        result = self.sum() / 5
        return result


cal1 = Calculator(1, 2, 3, 4, 5)
cal2 = Calculator(6, 7, 8, 9, 10)

print(cal1.sum())
print(cal1.avg())
print(cal2.sum())
print(cal2.avg())


def check(n):
    result = []
    for num in n:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10


print(check('1233345'))
print(check('12345'))
print(check('0123456789'))


dic = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}


def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


import re

s = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''

p = re.compile(r'(\w+\s+\d+[-]\d+)[-]\d+')
m = p.sub('\g<1>-####', s)
print(m)


def compress(str):
    prev_char = ""
    temp_str = ""

    for char in str:
        if prev_char == char:
            temp_str += '.'
        else:
            temp_str += '/'
            temp_str += char
            prev_char = char

    temp_array = temp_str.split('/')
    temp_array.remove('')

    result = ""

    for result_str in temp_array:
        result += "%s%i" % (result_str[0], len(result_str))

    return result

print(compress('aaabbcccccca'))
