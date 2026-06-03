import time
import random

def dice():
    while True:
        print('Вы кинули кубик...')
        time.sleep(2)
        player = random.randint(1, 6)
        print("Вам выпало: " + str(player))

        ai = random.randint(1, 6)
        print('Компьютер делает бросок...')
        time.sleep(2)
        print('У компьютера выпало: ' + str(ai))

        if player > ai:
            print('Вы выиграли!')
        elif player < ai:
            print('Вы проиграли.')
        else: 
            print('Ничья!')

        while True:
            count = input("Вы хотите выйти? (y/n): ").strip().lower()
            if count in ('y', 'n'):
                break
            else:
                print('Ваш выбор непонятен. Повторите ещё раз.')

        if count == 'y':
            print("Спасибо за игру!")
            time.sleep(2)
            exit() 
