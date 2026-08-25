import os


def show_current_folder():
	print("Joriy papka:", os.getcwd())
	print("Ichidagi elementlar:")
	for item in os.listdir():
		print(item)


def create_folder():
	folder_name = input("Papka nomini kiriting: ").strip()
	if os.path.exists(folder_name):
		print("Bu papka allaqachon mavjud.")
	else:
		os.mkdir(folder_name)
		print("Papka yaratildi.")


def check_file():
	file_name = input("Fayl nomini kiriting: ").strip()
	if os.path.exists(file_name) and os.path.isfile(file_name):
		print(f"{file_name} mavjud.")
	else:
		print(f"{file_name} mavjud emas.")


def show_file_size():
	file_name = input("Fayl nomini kiriting: ").strip()
	if os.path.isfile(file_name):
		print("Fayl hajmi:", os.path.getsize(file_name), "bytes")
	else:
		print("Bunday fayl mavjud emas.")


def identify_path():
	path_name = input("Nom kiriting: ").strip()
	if os.path.isdir(path_name):
		print("Bu papka.")
	elif os.path.isfile(path_name):
		print("Bu fayl.")
	else:
		print("Bunday fayl yoki papka mavjud emas.")


def write_students():
	students = ["Ali", "Vali", "Sardor", "Madina", "Aziza"]
	with open("students.txt", "w", encoding="utf-8") as file:
		file.writelines(student + "\n" for student in students)
	print("students.txt fayliga ma'lumot yozildi.")


def read_students():
	try:
		with open("students.txt", "r", encoding="utf-8") as file:
			print("Talabalar:")
			print(file.read(), end="")
	except FileNotFoundError:
		print("students.txt topilmadi. Avval 8-vazifani bajaring.")


def add_student():
	student_name = input("Yangi student: ").strip()
	with open("students.txt", "a", encoding="utf-8") as file:
		file.write(student_name + "\n")
	print("Student qo'shildi.")


def read_student_names():
	try:
		with open("students.txt", "r", encoding="utf-8") as file:
			students = [line.strip() for line in file if line.strip()]
	except FileNotFoundError:
		print("students.txt topilmadi.")
		return

	names = [student.split()[0] for student in students if student.split()]
	surnames = [student.split()[1] for student in students if len(student.split()) > 1]
	print("Names:", names)
	print("Surnames:", surnames)
	print("A bilan boshlanadigan ismlar:", [name for name in names if name.lower().startswith("a")])


def file_manager():
	while True:
		print("""\n===== FILE MANAGER =====
1. Papkadagi fayllarni ko'rish
2. Yangi papka yaratish
3. Yangi fayl yaratish
4. Faylni o'qish
5. Faylga yozish
6. Faylni o'chirish
7. Papkani o'chirish
8. Fayl hajmini ko'rish
9. Chiqish""")
		choice = input("Tanlang: ").strip()

		if choice == "1":
			for item in os.listdir():
				print(item)
		elif choice == "2":
			folder_name = input("Papka nomi: ").strip()
			if not os.path.exists(folder_name):
				os.mkdir(folder_name)
				print("Papka yaratildi.")
			else:
				print("Bu papka allaqachon mavjud.")
		elif choice == "3":
			file_name = input("Fayl nomi: ").strip()
			open(file_name, "a", encoding="utf-8").close()
			print("Fayl yaratildi.")
		elif choice == "4":
			file_name = input("Fayl nomi: ").strip()
			try:
				with open(file_name, "r", encoding="utf-8") as file:
					print("Fayl mazmuni:\n" + file.read())
			except FileNotFoundError:
				print("Fayl topilmadi.")
		elif choice == "5":
			file_name = input("Fayl nomi: ").strip()
			text = input("Matn: ")
			with open(file_name, "w", encoding="utf-8") as file:
				file.write(text + "\n")
			print("Faylga yozildi.")
		elif choice == "6":
			file_name = input("Fayl nomi: ").strip()
			if os.path.isfile(file_name):
				os.remove(file_name)
				print("Fayl o'chirildi.")
			else:
				print("Fayl topilmadi.")
		elif choice == "7":
			folder_name = input("Papka nomi: ").strip()
			if os.path.isdir(folder_name):
				os.rmdir(folder_name)
				print("Papka o'chirildi.")
			else:
				print("Bo'sh papka topilmadi.")
		elif choice == "8":
			show_file_size()
		elif choice == "9":
			break
		else:
			print("Noto'g'ri tanlov.")


def main():
	actions = {
		"3": show_current_folder,
		"4": create_folder,
		"5": check_file,
		"6": show_file_size,
		"7": identify_path,
		"8": write_students,
		"9": read_students,
		"10": add_student,
		"11": read_student_names,
		"12": file_manager,
	}
	print("3-11-vazifalardan birini tanlang (12 - File Manager, 0 - chiqish).")
	choice = input("Vazifa raqami: ").strip()
	if choice == "0":
		return
	action = actions.get(choice)
	if action:
		action()
	else:
		print("Noto'g'ri vazifa raqami.")


if __name__ == "__main__":
	main()