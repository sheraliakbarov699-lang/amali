students = [
    "Ali Valiyev",
    "Madina Karimova",
    "Sardor Toshmatov",
    "Aziza Qodirova",
    "Jasur Abdullayev",
    "Alisher Rustamov",
    "Malika Sobirova"
]

search_term = input("Ism kiriting: ").strip().lower()

# Katta-kichik harfga bog'liq bo'lmagan qidiruv
found_students = [s for s in students if search_term in s.lower()]

if found_students:
    print("\nTopilgan talabalar:")
    for s in found_students:
        print(s)
else:
    print("\nBunday student topilmadi.")