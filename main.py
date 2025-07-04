import logging
logging.basicConfig(level=logging.DEBUG) 

math_op = ['', '+', '-', '*', '/']
option = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))
logging.debug(f"Podane działanie to {num1} {math_op[option]} {num2}" )

sum = 0
if option == 1:
    sum = num1 + num2
elif option == 2:
    sum = num1 - num2
elif option == 3:
    sum = num1 * num2
elif option == 4:
    sum = num1 / num2

print(f"Twój wynik to {sum}")