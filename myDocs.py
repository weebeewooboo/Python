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
