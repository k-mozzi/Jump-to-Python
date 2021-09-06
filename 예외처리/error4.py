try:
    age = int(input('나이를 입력하세요: '))
except:
    print('숫자를 입력해주세요')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
# try문 수행중 오류가 발생하면 except절이 수행되고 오류가 없으면 else절이 수행된다.
