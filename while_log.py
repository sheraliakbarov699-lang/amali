print("--- BREAK misoli ---")
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1


print("\n--- CONTINUE misoli ---")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)