# This is a Python script to assign IDs to films that do not yet have an ID in the film database.
# This exists as a seperate file to allow user to run it independently from main.py

import csv

with open("films.csv", 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)

if 'ID' not in data[0]:
    data[0].append('ID')
    id_column_index = len(data[0]) - 1
else:
    id_column_index = data[0].index('ID')

existing_ids = set()
max_id = 0
for row in data[1:]:
    if id_column_index < len(row) and row[id_column_index]:
        try:
            id_value = int(row[id_column_index])
            existing_ids.add(id_value)
            max_id = max(max_id, id_value)
        except ValueError:
            pass

next_id = max_id + 1

for row in data[1:]:
    if id_column_index >= len(row) or not row[id_column_index]:
        while len(row) <= id_column_index:
            row.append('')
        
        while next_id in existing_ids:
            next_id += 1
        
        row[id_column_index] = next_id
        existing_ids.add(next_id)
        next_id += 1

with open("films.csv", 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Done!")