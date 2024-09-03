favorite_language = {
    'patryk' : 'c',
    'sara' : 'python',
    'wojtek' : 'rust',
    'zosia' : 'python'
}

people = ['wojtek', 'papież', 'krysia', 'sara', 'piotrek']

for imie in people:
    if imie in favorite_language:
        print(f"Witamy Ciebie {imie.title()}")
    else:
        print(f"{imie.title()} proszę o wypełnienie ankiety")