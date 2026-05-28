import time
import random
def dice():
    player=random.randint(1,6)
    print("Вам выпало: "+str(player))

    ai = random.randint(1,6)
    print('Компьютер думает...')
    time.sleep(2)
    print('У компьютера выпало: '+str(ai))

    if player>ai:
        print('Вы выйграли')
    elif ai<player:
        print('Вы проиграли')
    elif player==ai:
        print('Ничья')
    print("Вы хотите выйти? y/n")
    count=input()
    if count=='Y' or count=="y":
        exit()
    elif count=="N" or count=='n':
        pass
    else:
        print('Ваш выбро непонятен. Повторите еще раз')
