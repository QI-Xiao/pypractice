import random

total_round = 0
tot_guess = 0
while True:
    a = random.randint(1,100)
    one_guess = 0
    while True:
        b = int(input('请输入1-100的整数：\n'))
        one_guess += 1
        tot_guess += 1
        if one_guess > 9:
            print('guess too many times, you lost')
            tot_guess -= one_guess # 次数超过的整轮都不计入
            break
        if a > b:
            print('too small')
        elif a < b:
            print('too big')
        else:
            total_round += 1
            avr_guess = tot_guess / total_round
            print('bingo，已猜%d轮,平均%.1f次猜中' % (total_round, avr_guess))
            break
    gameagagin = input('again?(y/n)')
    if gameagagin == 'y':
        continue
    else:
        break
