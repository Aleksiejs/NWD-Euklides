
# coding: utf-8
#przykładowe liczby to 1989 i 867 wynik to 51

#przykład 1
a = int(input("Podaj pierwszą liczbę:\n"))
b = int(input("Podaj drugą liczbę:\n"))

while a > b:
    a = a - b
    while b > a:
        b = b - a
    
print (f"Największy wspólny dzielnik liczb 1989 i 867 to {a}")

#przykład2

a = int(input("Podaj pierwszą liczbę:\n"))
b = int(input("Podaj drugą liczbę:\n"))

while b != 0:
    c = a%b
    #zastąp a liczbą b, następnie b liczbą c
    a = b
    b = c
    #jeżeli wartość b wynosi 0, to a jest szukaną wartością NWD, w przeciwnym wypadku przejdź do kroku 1

print (f"Największy wspólny dzielnik liczb 1989 i 867 to {a}")
