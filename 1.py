notes = [
    "Сегодня мы работали с файлами Python.",
    "Научились сохранять текст.",
    "Узнали, как читать данные обратно."
]
with open("diary.txt", "w", encoding="utf-8") as f:
    for line in notes:
        print(line, file=f)
with open("diary.txt", "a", encoding="utf-8") as f:
    print("Следующее занятие – CSV и JSON.", file=f)
count = 0
with open("diary.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        count += 1
print("Количество записей:", count)
