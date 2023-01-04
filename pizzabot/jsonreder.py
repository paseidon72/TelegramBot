import json


d = []
with open("slova.txt", encoding='utf-8') as file:
        for i in file:
            n = i.lower().split('\n')[0]
            if n != '':
                d.append(n)

with open("combined.json", "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
        print('БД готова для передачи')

