while True:
    try:
        st_number = int(input('Введите первое число: '))
        nd_number = int(input('Введите второе число: '))
    except ValueError:
        print('Введите число НОРМАЛЬНОЕ число')
        st_number = int(input('Введите первое число: '))
        nd_number = int(input('Введите второе число: '))
    choice = input('Введите действие +,-,*,/,exit: ')
    def plus():
        sum_numbers = st_number + nd_number
        print(f'Сумма: {sum_numbers}')
    def difference():
        dif = st_number - nd_number
        print(f'Разность: {dif}')
    def multiplication():
        multi = st_number * nd_number
        print('Умножение:',multi)
    def division():
        try:
            div = st_number / nd_number
            print('Деление:',div)
        except ZeroDivisionError:
            print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ')
    if choice == '+':
        plus()
    elif choice == '-':
        difference()
    elif choice == '*':
        multiplication()
    elif choice == '/':
        division()
    elif choice == 'exit':
        print('Программа закрывается...')
        break
    else:
        print('Вы ввели неправильное значение!')
