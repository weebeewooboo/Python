toppings = []
prompt = "Proszę dodaj jaki dodatek do pizzy byś chciał"
prompt += "\nJeśli dodałeś już wszystko wpisz koniec:\n"
while True:
    new_topping = input(prompt)
    if new_topping == 'koniec':
        break
    print(f"\nDodano dodatek: {new_topping}")
    toppings.append(new_topping)

print("Twoje dodatki do pizzy:")
for top in toppings:
    print(f"\t {top}")