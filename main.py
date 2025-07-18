import logging
logging.basicConfig(level=logging.DEBUG) 

math_op = ['', '+', '-', '*', '/']

def add(a,b):
        sum = 0
        next_num = ''
        sum = a + b
        while True:
            try:
                next_num = input("Masz możliwość dodania więcej liczb. Wpisuj je kolejno zatwierdzając enterem, a ja skończysz to wpisz 'koniec': ")
                if next_num == 'koniec':
                    break
                else:
                    next_num = int(next_num)
                    sum += next_num
            except:
                logging.error(f"Podana wartość nie jest liczbą. Wpisz kolejne liczby zatwierdzając enterem lub jak chcesz skończyć to 'koniec': ")
                continue
        return sum

def subtract(a,b):
    return a - b

def multiply(a,b):
    sum = 0
    next_num = ''
    sum = a * b
    while next_num != 'koniec':
        try:
            next_num = input("Masz możliwość pomnożenia więcej liczb. Wpisuj je kolejno zatwierdzając enterem, a ja skończysz to wpisz 'koniec': ")
            if next_num == 'koniec':
                break
            else:
                next_num = int(next_num)
                sum *= next_num
        except:
            logging.error(f"Podana wartość nie jest liczbą. Wpisz kolejne liczby zatwierdzając enterem lub jak chcesz skończyć to 'koniec': ")
            continue
    return sum

def devide(a,b):
    return a / b

def calc_inputs():
    while True:
        try:
            option = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
            num1 = int(input("Podaj pierwszą liczbę: "))
            num2 = int(input("Podaj drugą liczbę: "))
            break
        except ValueError:
            logging.error("Podana wartość nie jest liczbą")
            continue
    logging.debug(f"Podane działanie to {num1} {math_op[option]} {num2}" )
    return num1, option, num2


num1, option, num2 = calc_inputs()
sum = 0
if option == 1:
    sum = add(num1, num2)
elif option == 2:
    sum = subtract(num1, num2)
elif option == 3:
    sum = multiply(num1, num2)
elif option == 4:
    sum = devide(num1, num2)


print(f"Twój wynik to {sum}")