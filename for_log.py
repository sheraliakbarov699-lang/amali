print("--- BREAK misoli ---")
for i in range(10):
    if i == 5:
        break
    print(i)



print("\n--- CONTINUE misoli ---")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)



print("\n--- Fruits list bilan break ---")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

print("\n--- Fruits list bilan continue ---")
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)