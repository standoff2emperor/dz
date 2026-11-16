import json
student = {
    "имя": "Алексей",
    "группа": "КБ-101",
    "навыки": ["Python", "Excel"],
    "уведомления": True
}
with open("participant.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=4)
with open("participant.json", "r", encoding="utf-8") as f:
    data = json.load(f)
data["навыки"].append("CSV")
data["уведомления"] = False
with open("participant.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
with open("participant.json", "r", encoding="utf-8") as f:
    res = json.load(f)
print("Имя:", res["имя"])
print("Группа:", res["группа"])
print("Навыки:", ", ".join(res["навыки"]))
if res["уведомления"]:
    print("Уведомления: Включены")
else:
    print("Уведомления: Выключены")
