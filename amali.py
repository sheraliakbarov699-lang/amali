names = ["ali", "vali", "sardor", "madina", "aziza"]


print([name.upper() for name in names])


print([name.capitalize() for name in names])


names_with_a = [name for name in names if "a" in name]
print("A bor ismlar:", names_with_a)


print("Nechta ismda bor:", len(names_with_a))

phones = [
    "+998 90 123 45 67",
    "+998 91 555 22 11",
    "+998 93 777 88 99",
    "+998 95 111 22 33"
]

cleaned_phones = [phone.replace(" ", "") for phone in phones]

print("Tozalangan raqamlar:")
for phone in cleaned_phones:
    print(phone)


for phone in cleaned_phones:
    if phone.startswith("+998"):
        print(f"{phone} -> Uzunligi: {len(phone)}")

        words = [
    "python",
    "java",
    "javascript",
    "go",
    "programming",
    "sql",
    "linux"
]


long_words = [word for word in words if len(word) >= 5]
print("5+ belgili so'zlar:", long_words)

# Eng uzun va eng qisqa so'z
print("Eng uzun so'z:", max(words, key=len))
print("Eng qisqa so'z:", min(words, key=len))


for word in words:
    print(f"{word} -> {len(word)}")

    emails = [
    "ali@gmail.com",
    "madina@yahoo.com",
    "sardor@gmail.com",
    "aziza@mail.ru",
    "jasur@gmail.com"
]


gmails = [email for email in emails if email.endswith("@gmail.com")]
print("Gmail foydalanuvchilari:", gmails)

usernames = [email.split("@")[0] for email in emails]
print("Usernamelar:", usernames)


print("Eng uzun username:", max(usernames, key=len))


products = [
    "iphone 15",
    "samsung s24",
    "macbook air",
    "redmi note 13",
    "airpods pro"
]

formatted_products = [product.capitalize() for product in products]
print("Formatlangan:", formatted_products)


print("Pro bor:", [p for p in products if "pro" in p])


print("iPhone bor:", [p for p in products if "iphone" in p])


for p in products:
    print(f"{p} -> {len(p)} belgi")


sorted_products = sorted(products, key=len)
print("Saralangan:", sorted_products)

students = [
    "Ali:85",
    "Madina:92",
    "Sardor:67",
    "Aziza:95",
    "Jasur:74"
]

names = [s.split(":")[0] for s in students]
scores = [int(s.split(":")[1]) for s in students]

print("names =", names)
print("scores =", scores)

print("Eng yuqori baho:", max(scores))
print("Eng past baho:", min(scores))


above_80 = [f"{names[i]}: {scores[i]}" for i in range(len(students)) if scores[i] > 80]
print("80 dan yuqori olganlar:", above_80)


average_score = sum(scores) / len(scores)
print("O'rtacha baho:", average_score)

users = [
    "ali:python123",
    "madina:admin456",
    "sardor:qwerty789",
    "aziza:hello123"
]

usernames = [u.split(":")[0] for u in users]
passwords = [u.split(":")[1] for u in users]

print("usernames =", usernames)
print("passwords =", passwords)


long_pass_users = [usernames[i] for i in range(len(users)) if len(passwords[i]) >= 8]
print("Paroli 8+ belgili foydalanuvchilar:", long_pass_users)


admin_passwords = [p for p in passwords if "admin" in p]
print("'admin' so'zi bor parol:", admin_passwords)


print("Eng uzun parol:", max(passwords, key=len))