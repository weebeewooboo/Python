# Dokumentacja

# CIĄGI TEKSTOWE

name = "jan kowalski"  # string - ciąg tekstowy, ciąg znaków

# string.title() - czyli stworzenie z str, nazwy czyli zmienienie pierwszych liter słów na wielką litere

print(name.title())  

# str.upper() - zmienienie na wielkie litery
# str.lower() - zmienienie na małe litery

print(name.upper())
print(name.lower())

# f"{str} {str}" - formatowanie dwóch stringów w jeden

first_name = "jan"
last_name = "Kowalski"
full_name = f"{first_name} {last_name}"
print(full_name)
 
# mozna tez uzyc FORMATU w print

print(f"Jestem {full_name.title()}")

# dodawanie białych znaków

# tabulator - \t

print(f"hi\t {full_name.title()}")

# znak nowej linie - \n

print(f"Hi \n {full_name.title()}")

# usuwanie białych znaków

# str.rstrip() - usuwanie białych znaków po prawej stronie

message = "jan kowal  "
message_2 = "ski"
print(f"uzycie metody str.rstrip() - {message.rstrip()}{message_2}")

# str.lstrip() - usuwanie białych znaków po lewej stronie

print("\tkarol".lstrip())

# str.strip() - usuwanie białych znaków zarówno po lewej jak i po prawej stronie

print(" \t kareol  \n".strip() + "jawef")

# usuwanie wszystkich białych znaków z ciągu tekstowego
import re

tekst = "Hello,   World!\nHow are you?\tI'm fine."
oczyszczony_tekst = re.sub(r'\s+', '', tekst)  # \s+ to jeden lub więcej białych znaków
print(oczyszczony_tekst)


#usuwanie prefiksów

# str.removeprefix - słuzy do usuwania prefiksów

google_url = "https://google.com"
print(google_url.removeprefix("https://"))

# str.removesuffix - słuzy do usuwania suffixów

plik = "work.txt"
print(plik.removesuffix(".txt"))

# uzywanie ' i "" w ciagu tekstowym

message = "It's a wonderful day"  # "  '  "
print(message)
# lub '  " " '
print('"The BOOK"')


# LICZBY

# operacje na liczbach

2+3
2-3
2/3
3*2
3**2
(2+3)*3

# zawsze liczba zmiennoprzecinkowa jest wynikiem działania nawet jeśli wynik jest liczbą całkowitą
2*0.1 
4/2
3.0 ** 2
2 * 3.0
1 + 2.0

# znaki podkreślania w liczbach - pominie znaki _ i pokaze całą liczbę

universal_age = 14_000_000_000
print(universal_age)

# przypisywanie wiele wartości

x,y,z = 0,0,0

# stała

MAX_DISTANCE = 5000

# LISTY
# numeracja listy zaczyna się od 0
rowery = ['trekingowy', 'miejski', 'górski', 'szosowy']

# wypisanie całej listy

print(rowery)

# wypisanie jednego elementu listy

print(rowery[0])

# działa tez indeksowanie poprzez liczby ujemne
# ostatni element listy to -1

print(rowery[-1])

# mozna tez wypisywanie litery z danej listy poprzez podwójne indeksowanie [][]
print(rowery[0][2]) 

#zmienianie elementów listy

rowery[0] = "dzieciecy"
print(rowery)

# list.append(zmienna) - dodawanie elementów do listy

rowery.append('trekingowy')
print(rowery)

# list.insert(index, zmienna) - wstawianie elementów do listy

rowery.insert(0,'uzywany')
print(rowery)

# del list[index] - usuwanie danego elementu listy

del rowery[0]
print(rowery)

# list.pop() - usuwanie ostatniego elementu listy zachowując jego wartość

motocykle = ['yamaha', 'suzuki', 'bmw']
last_owned = motocykle.pop()
print(last_owned)
print(motocykle)

# list.pop(index) - usuwanie dowolnego elementu z listy

motocykle.append(last_owned)
motocykle.pop(0)
print(motocykle)

# list.remove(zmienna) - usuwanie podanego elementu listy po jego wartości

motocykle.remove('bmw')
print(motocykle)

# list.sort() - sortowanie listy

# zwykłae uzycie metody sort() posegreguje liste alfabetycznie

cars = ['toyota', 'subaru', 'audi', 'bmw']
cars.sort()
print(cars)

# list.sort(reverse=True) - posortuje liste odwrotnie do alfabetycznie

cars.sort(reverse=True)
print(cars)

# sorted(list) - pozwala na wyświetlenie listy uporządkowanej alfabetycznie bez zmiany pierworodnej listy
#

print("Oto posortowana alfabetycznie lista: ")
print(sorted(cars))
print("Jak widać lista nie została zmieniona")
print(cars)
cars.sort()

# mozna tez posegregować liste odwrotnie alfabetycznie poprzez metode sorted(list,warunek)
print(sorted(cars,reverse=True))

# list.reverse() - odwraca elementy listy (zmienia liste)
print("Przed odwroceniem: ")
print(cars)
cars.reverse()
print("Po odwróceniu: ")
print(cars)

# len(list) - poznawanie długości listy 

print("Długość listy: " + str(len(cars)))


#4444444444444444444

# pętla for w liście

magicians = ["alicja", "karolina", "dawid"]

for magician in magicians:
    print(magician)


# range(od(włącznie), do) - wygenerowanie liczb "od"(włącznie) do "do"

for i in range(1,5):
    print(i)

# range(liczba) - wygenerowanie od 0 do "liczba"

for i in range(6):
    print(i)

# list(range()) - wygenerowanie listy liczb

numbers = list(range(6))
print(numbers)

# range(od,do, co ile) - wygenerowanie liczb o "co ile"

squares = []
for value in range(1,10,2):
    squares.append(value**2)
print(squares)

# stworzenie tego inaczej

squares = [values**2 for values in range(11)]
print(squares)

# min() max() sum()

liczby = list(range(11))
print(min(liczby))
print(max(liczby))
print(sum(liczby))

# list[od(włącznie), do] - wycinki listy

print(liczby[0:3])

# jeśli nie wpiszemy "od" to będzie od początku listy
print(liczby[:4])

# jeśli nie wpiszemy "do" to będzie do końca listy

print(liczby[3:])

# mozna tez uzywać ujemnego indeksowania 

print(liczby[-3:])

# iteracja przez wycinek

for n in liczby[:3]:
    print(n)

# list.sort() - mozna uzyc do posortowania listy liczbami od 
# najmniejszej do największej

# list.sort(reverse=True) - mozna uzyc do posortowania listy 
# liczbami od najwiekszej do najmniejszej

# kopiowanie listy

my_food = ['schabowy', 'rosół', 'gołąbki']
my_friend_food = my_food[:]

print("Moje ulubione jedzenie")
print(my_food)
print("Ulubione jedzenie mojego kolegi")
print(my_friend_food)

# niepoprawne skopiowanie

my_friend_food = my_food  # poniewaz teraz nowa lista wskazuje na tą 
#samą liste, więc nie są to dwie inne listy

my_friend_food.append("kotlet mielony")
my_food.append("kurczak")

print(my_food)
print(my_friend_food)

# krotka - czyli lista której nie da sie zmieniać, ale mozna sie do 
# niej dostawac

krotka = (200,500)
print(krotka[0])

# krotka jedno elementowa musi zawierać przecinek po jednym elemencie

krotka1 = (33,)

# iteracja po krotce

for krotk in krotka:
    print(krotk)

# nadpisanie krotki

krotka = (499,352)

# konstrukcja if
# sprawdzanie równości ==
for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.upper())

# sprawdzanie nierówności !=

something = "kotek"

if something != "piesek":
    print("Looking for " + something)
else:
    print("we have " + something)

# warnunki logiczne
# <= - mniejsze lub równe
# >= - wieksze lub równe
# > wieksze od
# < mniejsze od
# == takie same
# != nierówne
# warunek and warunek - dwa warunki muszą być True
# warunek or warunek - jeden z warunków musi być równy True

# in - sprawdzanie czy dana wartość jest w liście

numbers = list(range(10))
if 12 in numbers:
    print("mamy 12")
else:
    print("nie znaleźliśmy liczby 12")

# not in - sprawdzenie cyz dana wartość nie jest na liście

kotki = ['walef', 'mirek', 'wojtek']

if "misia" not in kotki:
    print("nie ma misia")

# if-elif-else

age = 12

if age <4:
    print("Bilet kosztuje 5 złotych")
elif age<18:
    print("Bilet kosztuje 15 złotych")
else:
    print("Bilet kosztuje 25 złotych")

# połączenie list - for - if

requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']
for requested_topping in requested_toppings:
    if requested_topping == "boczek":
        print("Przepraszamy ale nie mamy boczku")
    else:
        print(f"Dodaję {requested_topping}.")
print("\nTwoja pizza jest już gotowa!")

# sprawdzanie czy lista jest pusta 

requested_toppings = []

# lista zwraca True w "if" kiedy znajduje się w niej conajmniej jeden 
# element

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Dodajemy {requested_topping}")
else:
    print("Czy na pewno nie chcesz dodatków?")


# korzystanie z wielu list

available_toppings = ['pieczarki', 'oliwki', 'boczek', 'pepperoni', 'ananas', 'podwójny ser']
requested_toppings = ['pieczarki', 'frytki', 'podwójny ser'] 

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Dodajemy składnik: {requested_topping}")
    else:
        print(f"Nie posiadamy składnika: {requested_topping}")

# kopiowanie listy str zmieniając jej znaki

current_users = ["admin", "Jack", "Tomb", "Destroyer", "Kupa"]
cp_current_users = [user.lower() for user in current_users]


# SŁOWNIKI SŁOWNIKI SŁOWNIKI
# słowniki są nieograniczone
# słowniki są dynamiczne, czyli mozna je modyfikować i dodawać

alien_0 = {'color' : 'zielony', 'points': 5}

alien_0["x_position"] = 0
alien_0["y_position"] = 24
print(alien_0["color"])
print(alien_0["points"])
print(f"""Współrzędne zabitego obcego: 
{str(alien_0['x_position'])}x{str(alien_0['y_position'])}""")

# praca z pustym słownikiem

alien_1 = {}

alien_1['color'] = "czerwony"
alien_1['points'] = 15
print(alien_1)

# modyfikowanie wartość - uzyłem kodu z góry

alien_1['color'] = "zółty"
alien_1['points'] = 10
print(alien_1)

# usuwanie pary z słownika

del alien_1["color"]
print(alien_1)

# tworzenie słowników wielu zmiennych

favorite_language = {
    'patryk' : 'c',
    'sara' : 'python',
    'wojtek' : 'rust',
    'zosia' : 'python'
}

print(f'Ulubiony język programowania Zosi:: {favorite_language['zosia'].title()}')

# słownik.get('pierwsza część pary', 'wartość podstawowa)
# jeśli w danym słowniku nie ma wartośc przypisanej do pary to wyświetli
# wartość podstawową, natomiast gdy jest wyświetli wartość normalna

alien_1['speed'] = 12
speed_value = alien_1.get('speed', 'Nie podano wartośći')

print(speed_value)

# iteracja przez słownik


# iteracja przez pare klucz-wartość

user_0 = {
'username': 'jkowalski', 
'first': 'jan',
'last': 'kowalski',
}

# słownik.items() - wartością zwracaną jest lista par klucz-wartość

print(user_0.items())

for k, v in user_0.items():
    print(f'klucz {k}')
    print(f'wartość {v}')

# iteracja przez wszystkie klucze słownika

# mozna tez uzyc:

# for k in user_0:
for k in user_0.keys():
    print(f'Klucz: {k}')


# przykład - keys()

friends = ['patryk', 'wojtek']

for name in favorite_language:
    print(f'Witamy Ciebie {name}')
    if name in friends:
        print(f"""Cześć przyjacielu {name.title()}, wiemy ze Twoim ulubionym
              językiem jest {favorite_language[name].title()}""")
        
# przykład keys()

if 'elzbieta' not in favorite_language:
    print("Elzbieta proszę weź udział w ankiecie")

# iteracja przez uporządkowane klucze słownika

print("Zgodnie z kolejnością alfabetyczną\n")
for name in sorted(favorite_language):
    print(f"HI {name}")

# iteracja prrzez wszystkie wartosci słownika

for v in user_0.values():
    print(f'Wartość: {v}')

# iteracja poprzez uzycie set()

# set() - działa tak ze wychwyci tylko unikatowe wartosci, takie co sie 
# nie powtarzają

print("\nOto jakie jezyki programowania zostały wymienione")
for lang in set(favorite_language.values()):
    print(lang.title())

# zbiory - czyli zbiór wartości 
# jezeli natomiast wywołamy zbiór pokaza sie tylko unikatowe wartosci
# czyli kazda wartosc nawet jeśli się powtarza, wyświetli się tylko raz

print("\n WYŚWIETLENIE ZBIORU")
languages = {'python', 'c', 'rust','python', 'c', 'c++'}

print(languages)

# ZAGNIEŻDŻENIE

print("\n WYŚWIETLENIE ZAGNIEŻDŻENIA\n")
alien_0 = {'color': 'zielony', 'points': 5} 
alien_1 = {'color': 'żółty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# tworzenie floty wrogów

print("\n Tworzenie floty wrogów\n")

aliens = []

for i in range(5):
    new_alien = {'color' : 'zielony', 'points' : 5, 'speed' : 'wolno'}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)

print(f"\nCałkowita liczba wrogów to: {len(aliens)}")

# praca z takimi wrogami - przykład

for alien in aliens[:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['points'] = 10
        alien['speed'] = 'średnio'
    print(alien)

# lista w słowniku

pizza = {
    'crust' : 'grube',
    'toppings' : ['pieczarki', 'dodatkowy ser']
}
print('\nLista w słowniku\n')
print(pizza['crust'])
print(pizza['toppings'])

# program - przykład

favorite_languages = {
    'janek': ['python', 'rust'], 
    'sara': ['c'],
    'edward': ['rust', 'go'], 
    'paweł': ['python', 'haskell'],
}

for name, language in favorite_languages.items():
    print(f"\n Ulubione języki programowania {name.title()} to: ")
    for lang in language:
        print(f'\t{lang.title()}')

# słownik w słowniku

users = { 
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein', 
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'maria',
        'last': 'skłodowska-curie',
        'location': 'paryż',
        },
}

for user, user_info in users.items():
    print(f"Witamy użytkownika: {user}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\t Imie i Nazwisko: {full_name.title()}")
    print(f"\t Lokacja: {location.title()}")


# DANE WEJŚCIOWE I PĘTLA WHILE

# input()

#name = input("Podaj swoje imie: ")
print(name.title())

# tworzenie dłuższych komunikatów

prompt = '''Jeżeli powiesz nam, kim jesteś, spersonalizujemy wyświetlany 
komunikat.'''
prompt += '\nJak masz na imie: '

#name = input(prompt)
print(f"\nWitaj, {name.title()}!")

# int() - formatowanie danych do zmiennej int

#age = int(input("Podaj swój wiek: "))

#if age > 12:
    #print("Nie jesteś już dzieckiem!")

# % - modulo - zwraca resztę z dzielenia
# można użyć naprzykład do tego by rozróżniać liczby nieparzyste od parz

#number = int(input("Podaj jakąś liczbę by sprawdzić czy jest parzysta: "))

#if number%2==0:
    #print("Liczba jest parzysta!")
#else:
    #print("Liczba jest nieparzysta!")

# pętla while

current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

# program umożliwiający użytkownikowi skończyć program kiedy będzie chciał

prompt = "Powiedz nam coś o sobie gamoniu:\nJeśli chcesz skończyć program napisz koniec. "

message = ''
while message != 'koniec':
    message = input(prompt)
    if message != 'koniec':
        print(message)

# używanie flagi

prompt = "Powiedz nam coś o sobie gamoniu:\nJeśli chcesz skończyć program napisz koniec. "

active = True
while active:
    message = input(prompt)
    if message == 'koniec':
        active = False
    else:
        print(message)

# używanie break - powoduje zakończenie się pętli
# można użyć w: while i for

prompt = "Powiedz nam coś o sobie gamoniu:\nJeśli chcesz skończyć program napisz koniec. "


while True:
    message = input(prompt)
    if message == 'koniec':
        break
    else:
        print(message)

# używanie continue - powoduje automatyczne przeskoczenie do dalszej
# iteracji pętli bez wykonywanie następnych poleceń w danej pętli

current_number = 0

while current_number<10:
    current_number +=1
    if current_number%2 == 0:
        continue
    
    print(current_number)


# przenoszenie elementów z jednej listy na drugą

unconfirmed_users = ['Alicja', 'Bartek', 'Katarzyna']
confirmed_users = []

while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print(f"Zweryfikowano użytkownika: {confirmed_user}")
    confirmed_users.append(confirmed_user)

print("Lista zweryfikowanych użytkowników: ")
for user in confirmed_users:
    print(f"\t{user}")
    

# usuwanie z listy wszystkich egzemplarzy danej wartości

pets = ['pies', 'kot', 'pies', 'złota rybka', 'kot', 'królik', 'kot']
print(pets)

while 'kot' in pets:
    pets.remove('kot')

print(pets)

# umieszczanie w słowniku wartości wprowadzonych przez użytkownika

responses = {}
active = True

while active:
    name = input("Podaj nam swoje imie do ankiety: ")
    response = input("Jaki język programowania lubisz?\n")

    responses[name] = response

    repeat = input("Wpisz 'tak' jeśli następna osoba chce rozpocząć ankiete\n")

    if repeat.lower() != 'tak':
        active = False

print("Oto wyniki naszej ankiety:")
for name,response in responses.items():
    print(f"{name.title()} bardzo lubi język programowania: {response}")

# FUNKCJE

# definiowanie funkcji

def greet_users():
    # docstring '''komentarz''' - jego zadaniem jest opisanie funkcji
    #ego rodzaje komen- tarze są ujęte w potrójny cudzysłów, który jest 
    # wyszukiwany przez Pythona podczas generowania dokumentacji dla 
    # funkcji zdefiniowanych w Twoich programach.
    '''Wyświetla proste powitanie'''
    print("Witaj")

greet_users()

# przekazywanie informacji do funkcji

def user_age(age):
    '''Wyświetla informacje o wieku użytkownika'''
    print(f"Wiek użytkownika: {age}")

user_age(13)

# przekazywanie argumentów

# argumenty pozycyjne

def describe_pet(animal_type, pet_name):
    '''Wyświetla informacje o Twoim zwierzaku'''
    print(f"Rasa Twojego zwierzaka to: {animal_type}")
    print(f"Twój {animal_type} ma na imie {pet_name.title()}")

describe_pet("pies","Jack")

# argumenty w postaci słów kluczowych
# nie trzeba dbać o kolejność argumentów funkcji
describe_pet(animal_type='pies',pet_name='jack')

# wartości domyślne
# jeśli zostaną podane argumenty python zignoruje wartości domyślne

def describe_pet(pet_name, animal_type ='pies'):
    '''Wyświetla informacje o Twoim zwierzaku'''
    print(f"Rasa Twojego zwierzaka to: {animal_type}")
    print(f"Twój {animal_type} ma na imie {pet_name.title()}")

describe_pet("Jack")
describe_pet("miś", 'kot')

# wartość zwrotna - return

def get_formatted_name(first_name, last_name):
    '''Zwraca elegancko sformatowane pełne imie i nazwisko'''
    full_name = f'{first_name.title()} {last_name.title()}'
    return full_name

print(get_formatted_name('karol', 'wojtyła'))

# definiowanie argumentu jako opcjonalnego

def get_formatted_name(first_name, last_name, middle_name=''):
    '''Zwraca elegancko sformatowane pełne imie i nazwisko'''
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f'{first_name.title()} {last_name.title()}'
    return full_name

print(get_formatted_name('karol','wojtyła'))
print(get_formatted_name('jan', 'Drugi', 'Paweł'))

# zwrot słownika

def build_person(first_name, last_name, age=None):
    '''Budowanie osoby czyli słownika'''
    person = {'first': first_name.title(), 'last' : last_name.title()}
    if age:
        person['wiek'] = age
    return person

print(build_person('karol', 'Wojtyła'))
print(build_person('karol', 'Wojtyła',67))


# używanie funkcji i pętli while 

while True:
    print("Proszę podać imie i nazwisko:")
    print("Wpisz 'q' w dowolnym momencie by zakończyć pracę")
    f_name = input("Imie: ")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break
    formated_name = get_formatted_name(f_name,l_name)
    print(f"Twoje imie i nazwisko: {formated_name}")
    break

# przekazywanie listy

users = ['wojtek', 'paweł', 'piotrek']
def greet_users(names):
    '''Wyświetla przywitanie dla ludzi'''
    for name in names:
        print(f"Witaj, {name.title()}")

greet_users(users)

# modyfikowanie listy w funkcji

unprinted_designs = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_designs = []

def print_models(unprinted_designs, completed_designs):
    '''Funkcja zajmująca się wydrukiem modeli'''
    while unprinted_designs:
        complete_model = unprinted_designs.pop()
        print(f"Trwa drukowanie modelu: {complete_model}")
        completed_designs.append(complete_model)
    

def show_printed(completed_designs):
    for design in completed_designs:
        print(f"Wydrukowano model: {design}")

# używamy tutaj przy liście [:], aby funkcja nie modyfikowała wartości
# natomiast przekaże funkcji tylko jej kopię, pozostawiajac oryginał 
# bez naruszenia !!! (MARNUJE CZAS I PAMIĘĆ)

# ważne jest by jednak korzystać z prawdziwej funkcji ponieważ program 
# wtedy wykorzystuje więcej pamięci na stworzenie nowej kopi
# i pracowanie na niej
print_models(unprinted_designs[:],completed_designs)
show_printed(completed_designs)
print(unprinted_designs)
print(completed_designs)

# przekazywanie dowolnej liczby argumentów 
# def nazwa_funkcji(*argument)

def make_pizza(*toppings):
    '''Funkcja tworząca pizze'''
    print("Przygotowuj pizze z następującymi dodatkami:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('piieczarki')
make_pizza('pieczarki','dodatkowy ser', 'ketchup')

# argumenty pozycyjne i przekazywanie dowolnej liczby argumentów

def make_pizza(size, *toppings):
    '''Funkcja tworząca pizze'''
    print(f"Przygotowuj pizze {size}cm z następującymi dodatkami:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(40,'piieczarki')
make_pizza(30,'pieczarki','dodatkowy ser', 'ketchup')

# używanie dowolnej liczby argumentów w postaci słów kluczowych

def build_profile(first,last, **user_info):
    '''Budowa słownika zawierającego wszelkie informacje o użytkowniku'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton',
                             field = 'fizyka')

print(user_profile)

# przechowywanie funkcji w modułach
# jest to przechowywanie funkcji w innym pliku określanym modułem, a 
# następnie importować ten moduł do programu, w którym mają być wywoływane
# funkcje danego modułu

# import całego modułu 

import pizza

pizza.make_pizza(40, 'pepperoni')
pizza.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# import określonych funkcji

# syntax 
# from nazwa_modułu import nazwa_funkcji

# można też wiele funkcji

# from nazwa_modułu import nazwa_funkcji_0, nazwa_funkcji_1,
# nazwa_funkcji_2

# przykład

from pizza import make_pizza

make_pizza(40, 'pepperoni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# użycie słowa kluczowego as w celu zdefiniowania aliasu funkcji

# gdy nazwa importowanej funkcji może kolidować z nazwą funkcji
# istniejącej już w programie, lub też ta nazwa jest zbyt długa, 
# wówczas można zastosować skrót 

from pizza import make_pizza as mp

mp(40, 'pepperoni')
mp(30, 'pieczarki', 'zielona papryka', 'podwójny ser')







    