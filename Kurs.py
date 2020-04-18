import calendar as c #importujemy kalendarz
import random as r
import requests as re
from bs4 import BeautifulSoup as BF

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:08:11 2020

@author: Nataniel Antosik
"""

#pytania odpowiedź python wersja 3
#pytanie print(word[:2]) idzie do 2 elementu od 0 do 1
#lower() zamienia wszystkie znaki duże na małe
#print(10/4) = 2.5
#print(10//4) = 2
#users = ['michal','anna','piotr'] #lista
#users.append('michal')
#print(users.append('michal')) # dodaje do listy element
#słownik ma klucz i wartosc
#w liscie jest indeks i wartosc


'''
#zadanie 1
print('Hello world')

#zadanie 2
x = int(input('Podaj pierwszą liczbę całkowitą:\n')) #\n nowa linia
y = int(input('Podaj drugą liczbę całkowitą:\n'))
print('Iloczyn liczb: ',x*y)

#zadanie 3
x = int(input('Podaj pierwszą liczbę całkowitą:\n'))
y = int(input('Podaj drugą liczbę całkowitą:\n'))
print('Suma liczb: ', x+y)

#zadnie 4
x = 1000 
y = '1000'
print(x)
print(y)
print(1000)
print('1000')

#zadanie 5
print(100*30000)

#zadanie 6
x = input('Podaj wyraz: ')
print(x[0:2]) #pierwsze 2 litery
#print(x[0]+x[1])
print(x[:2])
print(x[-1]) #ostatnia litera

name = 'Nataniel'
index = 0
index2 = -1
print("Pierwsza litera",name[index])  #pierwszy element, print[0]
print("Ostatnia litera",name[index2]) #ostatni element, print[-1]

#zadanie 7
name = input('Podaj imie: ')
if name [-1] == 'a':
    if name == 'Kuba' or name == 'Barnaba':
        print('Mężczyzna')
    else:
        print('Kobieta')  
else:
    print('Mężczyzna')
        
#zadanie 8
x = int(input('Podaj liczbę '))
print('Ostatnia cyfra to',x%10) #reszta z dzielenia modulo 10 zawsze będzie pokazywać ostatnią wartoć poniważ będzie dzielić liczby
#X = int(str(x)[-1])
#print(X)

#zadanie 9
print("\n",c.month(2016,2)) #c jest jak kalendarz

#zadanie 10
rok = int(input('Podaj rok: '))
miesiac = int(input('Podaj numer miesiaca: '))
print("\n",c.month(rok,miesiac))

#zadanie 11
wyraz = input('Podaj nazwę: ')
if wyraz.lower() == 'akademia': # lower() ta funkcja zamienia wszystkie duże litery na małe
    print('Poprawne hasło')
else:
    print('Nie poprawne hasło!')

#zadanie 12
# lub = or, i = and
x = int(input('Podaj liczbe: '))
if x%3 == 0:
    print('Liczba jest podzielna przez 3')
elif x%5 == 0: #else if
    print('Liczba jest podzielna przez 5')
else:
    print('Liczba nie jest podzielna przez 5 ani 3')
    
#if x%3 == 0 or x%5 == 0:
#    print("Liczba jest podzielna przez 3 lub 5")
#else:
#    print("Liczba nie jest podzielna przez 3 lub 5")

#zadanie 13
wiek = int(input('Podaj wiek: '))
if wiek >= 18:
    print("Jestes pelnoletni")
else:
    print("Nie jestes pelnoletni")
    
#zadanie 14
for i in range(1,11): #od czegos do czegos domyslnie jak jest 1 liczba to indeksuje od 0
    print(i)
    
#zadanie 15
print(" ")
for i in range(20,0,-1): #3 wartosc to krok 
    print(i)
    
#zadanie 16
print(" ")    
for i in range(1,11): 
    print("*")
print("Inna opcja",'*'*10) #mnożymy * razy 10 i też wypisze nam 10 gwiazdek   

#zadanie 17
print(" ")    
for i in range(2,51):
    print(i)
#duży lotek
#1 do 49, losowanych jest 6 liczb
#wylosuj 6 liczb z duzego lotka
print (" ")
for i in range(6):
    print(r.randrange(1,50))
#zadanie 18
#słownik ma klucz i wartosc
#JSON dane z tego 
#dictionary = { '5': 'pięć', '6': 'szesc', '1': 'jeden' }
#print(dictionary['5'])
dictionary = {'czesc': 'hello', 'mama': 'mother', 'tata': 'father', 'pies': 'dog'}
dictionary['koniec'] = 'end'
polish_word = input('Podaj słowo po Polsku ')
if polish_word in dictionary:
    print(dictionary[polish_word])
else:
    print('Brak tego słowa')

#zadanie 19
def l_pierwsza(n):
    if n == 2:                  #sprawdzamy czy liczba jest 2 bo to szczególny przypadek
        return True
    if n % 2 == 0 or n <= 1:    #jeżeli jest parzysta lub mniejsza bądź równa 1 to nie jest liczbą pierwsza
        return False

    pierw = int(n**0.5) + 1     #sprawdzamy czy liczba ma dzielnik
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True
print(l_pierwsza(7))
'''
#zadanie 20
url = 'https://www.pracuj.pl/praca/python;kw?rd=0'   
page = re.get(url) #dostań się do strony 
soup = BF(page.content,'html.parser') #przetwarzamy dane ze strony
print(soup.title)
#<span class="results-header__offer-count-text-number">256</span>
element = soup.find('span',class_="results-header__offer-count-text-number") #chcemy znaleźć element klase span
print('Liczba ofert pracy w Pythonie to ', element.text) #text musi być bo by pokazło kod z html

#zadanie 21
 
  
#zadanie 22
#zadanie 23
#zadanie 24
#zadanie 25