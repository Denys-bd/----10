import os

# Отримуємо шлях до поточної папки
folder = os.getcwd()

print("Вміст поточної папки:")
print(folder)

# Виводимо список файлів і папок
for item in os.listdir(folder):
    print(item)

# Знаходимо всі файли з розширенням .txt
txt_files = [
    item for item in os.listdir(folder)
    if item.lower().endswith(".txt")
    and os.path.isfile(os.path.join(folder, item))
]

# Перевіряємо, чи є TXT-файли
if txt_files:
    print("\nЗнайдені TXT-файли:")
    for item in txt_files:
        print(item)

    answer = input("Видалити ці файли? (так/ні): ").strip().lower()

    if answer == "так":
        for item in txt_files:
            os.remove(os.path.join(folder, item))
            print(f"Файл {item} видалено.")

        print("Видалення завершено.")
    else:
        print("Видалення скасовано.")
else:
    print("\nTXT-файлів у поточній папці немає.")