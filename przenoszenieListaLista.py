unconfirmed_users = ['Alicja', 'Bartek', 'Katarzyna']
confirmed_users = []

while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print(f"Zweryfikowano użytkownika: {confirmed_user}")
    confirmed_users.append(confirmed_user)

print("Lista zweryfikowanych użytkowników: ")
for user in confirmed_users:
    print(f"\t{user}")
    