print('Это простейший калькулятор.'
      '\nВы можете складывать (+), вычитать(-), умножать(*) и делить(/) числа.')
while True:
    def nmbr():
        n = int(input('Введите число: '))
        return n

    a = nmbr()
    m = input('Введите знак +, -, *, /: ')
    b = nmbr()

    if m == '+':
        print(a + b)
    elif m == '-':
        print(a - b)
    elif m == '*':
        print(a * b)
    elif m == '/':
        try:
            print(a / b)
        except ZeroDivisionError:
            print('Нельзя делить на ноль')

    CC = input('Хотите завершить работу с калькулятором? да/нет: ')
    if CC == 'да':
        break
    else:
        continue
