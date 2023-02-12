#Игра, вы загадывайте число и программа угадать это число.
print("Введите число:")
n = int(input())
if n > 100 or n < 0:
    print('Надо загадывать числа от 1 до 100.')
    exit()
#if n > 0 and n <= 100:
#    print('Надо загадывать числа от 1 до 100.')
#    exit()
s = 50
a = 50
tf = ''
for i in range(99999999999999):
    print("Ваше число", a)
    # print(a)
    print("Да(y), Больше(>), Меньше (<)")
    ans = input()
    if ans == 'y':
        print('Вы загадали число:', a)
        break
    elif ans == '>':
        s = s // 2
        d = s % 2
        a = a + s
        s += d
    elif ans == '<':
        s = s // 2
        d = s % 2
        a = a - s    
        s += d
