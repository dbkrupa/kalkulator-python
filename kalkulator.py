print("Kalkulator prosty")

a = float(input("Podaj pierszą liczbe"))
dzialanie = input("Podaj działanie (+, -, *, /): ")
b = float(input("Podaj drugą liczbe"))

if dzialanie == "+":
    print("Wynik: ", a + b)
elif dzialanie == "-":
    print("Wynik: ", a - b)
elif dzialanie == "*":
    print("Wynik: ", a * b)
elif dzialanie == "/":
    if b != 0:
        print("Wynik: ", a / b)
    else:
        print("Nie dziel przez 0!")
