import logging
logging.basicConfig(level=logging.DEBUG) 

math_op = ['', '+', '-', '*', '/']
option = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))
logging.debug(f"Podane działanie to {num1} {math_op[option]} {num2}" )

sum = 0
next_num = ''
if option == 1:
    sum = num1 + num2
    while next_num != 'koniec':
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
elif option == 2:
    sum = num1 - num2
elif option == 3:
    sum = num1 * num2
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
elif option == 4:
    sum = num1 / num2

print(f"Twój wynik to {sum}")