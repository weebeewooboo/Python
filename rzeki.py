rzeki = {
    'nil' : 'egipt',
    'wisla' : 'polska',
    'amazonka' : 'peru', 
    'jangcy' : 'chiny'
}

for rzeka, kraj in rzeki.items():
    print(f"{rzeka.title()} przepływa przez {kraj.title()}")

for rzeka in rzeki:
    print(f"{rzeka.title()}")

for kraj in rzeki.values():
    print(f"{kraj.title()}")

