#Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).
import os
def clear(): return os.system('cls')


clear()
Q = int(input('Введите номер четверти: '))
if Q == 1:
    print('X>0,Y>0')
elif Q == 2:
    print('X<0,Y>0')
elif Q == 3:
    print('X<0,Y<0')
elif Q == 4:
    print('X>0,Y<0')
else:
    print('Ошибка ввода!')
