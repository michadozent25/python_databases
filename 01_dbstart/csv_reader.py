import csv
import os

# Workaround - Pfad-Probleme
script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir,'users.csv')

with open (full_path,newline='',encoding='utf-8')  as csvfile:
    reader = csv.DictReader(csvfile,fieldnames=range(2))
    for row in reader:
        #print(row['name'], row['email']) # 


# ---------------- ohne Überschriften im csv ------------------------
# with open (full_path,newline='',encoding='utf-8')  as csvfile:
#     reader = csv.DictReader(csvfile,fieldnames=range(2))
#     for row in reader:
#         print(row[0],row[1])
