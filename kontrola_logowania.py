current_users = ["admin", "Jack", "Tomb", "Destroyer", "Kupa"]
new_users = ["Paul", "jack", "witek"]
cp_current_users = [user.lower() for user in current_users]
cp_new_users = [new.lower() for new in new_users]
if current_users:
    for new in new_users:
        if new.lower() in cp_current_users:
            print(f"Nie mozna wykorzystac nazwy {new}")
        else:
            print(f"Mozna wykorzystac nazwe {new}")
else:
    if not new_users:
        print("Musimy znaleźć nowych uzytkownikow!")

