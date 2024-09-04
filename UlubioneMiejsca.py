people = {
    'karol' : ['Japonia', 'Norwegia', 'Bali'],
    'Rozalia' : ['Grecja', 'Japonia', 'Wietnam'],
    'Kuba' : ['Anglia', 'Polska', 'Szwecja']
}

for k,v in people.items():
    print(f"\n Ulubione kraje {k.title()}:")
    for country in v:
        print(f"\t{country}")