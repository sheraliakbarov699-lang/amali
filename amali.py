import os

path = input("Nom kiriting: ").strip()

if os.path.exists(path):
    if os.path.isdir(path):
        print("Bu papka.")
    elif os.path.isfile(path):
        print("Bu fayl.")
else:
    print("Bunday fayl yoki papka mavjud emas.")