#Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import os
def clear(): return os.system('cls')


clear()
print('  ')
x = None
y = None
z = None
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
           if (not (x or y or z)) == (not x and not y and not z):
            print(x, y, z)
            print('True')
           else:
            print(x, y, z)
            print('false')
