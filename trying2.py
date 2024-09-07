def make_pizza(size, *toppings):
    '''Funkcja tworząca pizze'''
    print(f"Przygotowuj pizze {size}cm z następującymi dodatkami:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(40,'piieczarki')
make_pizza(30,'pieczarki','dodatkowy ser', 'ketchup')
