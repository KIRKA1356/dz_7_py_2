import sys

def write_code(x):
    f = open(f'{x}.txt', 'w')
    code = input('Введите событе, который нужно перезаписать: ')
    f.write(code)
    f.close

def read_code(x):
    y = open(f'{x}.txt', 'r')
    code_2 = str(y.readline())
    y.close
    return code_2

def update_code(x):
    f = open(f'{x}.txt', 'a')
    code = input(f'Введите событие, который нужно дописать: ')
    f.write(code)
    f.close


x = 0
while x !=1:
    first_item = input("Введите операцию короую хотите выполнить, где w - перезапись событий на день, a-дополнить записи на день, r-посмотреть записи на день, 10 - выход из дневника: ")

    if first_item == 'w':
        x = int(input("Введите порядковый номер дня недели, на который вы ходите сделать запись, если вам неободио закртыть заполение расписания введите 10: "))
        write_code(x)
    elif first_item == 'a':
        x = input("Введите порядковый номер дня недели, на который вы ходите сделать дополнительную запись, если вам неободио закртыть заполение расписания введите 10: ")
        update_code(x)
    elif first_item == 'r':
        read_code(x)
    elif first_item == '10':
        sys.exit("Вы вышли из дневника")









