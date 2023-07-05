import math 
import datetime

#Napisz funkcję, która zwróci wartość pola powierzchni koła
#o zadanym promieniu (według wzoru `PI * r^2`, gdzie `r` to promień).

def pole_kola(r):
    pole_kola = (math.pi) * (r ** 2)
    print(pole_kola)

pole_kola(1)

#Napisz funkcję, która przyjmuje dwie daty jako argumenty.
#Jeżeli druga data jest mniejsza od pierwszej, funkcja powinna zwrócić
#`None`.  W przeciwnym wypadku funkcja powinna zwrócić liczbę sekund
#dzielącą obie daty.  Zwróć uwagę, że różnica może być większa niż jedna
#doba.  W takim wypadku liczbę dni należy zamienić na sekundy.

#a=datetime.datetime()
#b=datetime.datetime()

def difference_bet_dates (a, b):
    if b < a :
        return None
    else:
        difference = b-a
        print(difference.seconds)

difference_bet_dates()
#difference_bet_dates(2023, 2021)