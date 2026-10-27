import re

# Відкриваємо файл із текстом
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Знаходимо всі слова та переводимо їх у нижній регістр
words = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", text.lower())

# Підраховуємо частоту кожного слова
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Записуємо результат у файл freq.txt
with open("freq.txt", "w", encoding="utf-8") as file:
    for word, count in sorted(frequency.items()):
        file.write(f"{word}={count}\n")

print("Підрахунок слів завершено.")
print("Результат записано у файл freq.txt.")