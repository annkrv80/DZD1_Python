#Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, является ли этот день выходным.
import os
def clear(): return os.system('cls')


clear()
a = int(input('Введите день недели '))
if 1 <= a <= 5:
    print('Heт')
elif a == 6 or a == 7:
    print('Да')
elif a == 0 or a > 7:
    print('Надо бы знать что в неделе всего 7 дней')
