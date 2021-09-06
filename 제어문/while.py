treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1  # (treeHit += 1)과 같음
    print(f'나무를 {treeHit}번 찍었습니다.')
    if treeHit == 10:
        print('나무가 넘어갑니다.')


prompt = '''
1. Add
2. Del
3. List
4. Quit

enter number: '''
number = 0
while number != 4:
    print(prompt)
    number = int(input())


coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee - 1
    print(f'커피가 {coffee}개 남았습니다.')
    if coffee == 0:
        print('커피가 다 떨어졌습니다.' '\n')
        break


coffee = 10
while True:
    money = int(input('돈을 넣어 주세요: '))
    if money == 300:
        print('돈을 받았으니 커피를 줍니다.')
        coffee = coffee - 1
    elif money > 300:
        print(f'거스름돈 {money-300}원을 주고 커피를 줍니다.')
        coffee = coffee - 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


while True: # 짝수가 나올 때까지 결과를 출력하는 코드
    a = int(input('숫자를 넣어주세요: '))
    if a % 2 != 0:
        print('홀수입니다.')
    else:
        print('짝수입니다.')
        break