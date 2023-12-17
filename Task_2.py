def convert(filepath, newfilepath):
    import json

    # Открытие отчета
    with open(filepath, "r") as f:
        data = json.load(f)
        info = {
            "vulnerabilities": []
        }

        # Считывание данных
        for i in data["site"][0]["alerts"]:
            name = i["alert"]
            count = i["count"]
            info["vulnerabilities"].append({"name": name.strip(), "count": int(count)})

        # Запись данных в новый файл
        with open(newfilepath, "w+") as n:
            n.write(json.dumps(info, indent=3, ensure_ascii=False))


# Файл с отчетом
file = r"D:\Work\PT\PT-Intensive\Int16\2023-12-18-ZAP-Report-.json"
# Имя нового файла
newfile = r"D:\Work\PT\PT-Intensive\Int16\2023-12-18-ZAP-Report-converted.json"

# Вызов функции конвертации
convert(file, newfile)
