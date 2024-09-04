dog_0 = {
    'name' : 'papi',
    'owner' : 'karol',
    'age' : 1
}
dog_1 = {
    'name' : 'jack',
    'owner' : 'zosia',
    'age' : 13
}

pets = [dog_0, dog_1]

for pet in pets:
    print("\nInformacje o zwierzaku:")
    for k,v in pet.items():
        print(f"{k} : {v}")