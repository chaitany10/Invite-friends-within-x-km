import csv
from entries.models import Entry

with open('friends.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
            a = Entry()
            a.name=row["name"]
            a.user_id=int(row["user_id"])
            a.latitude = float(row["ï»¿latitude"])
            a.longitude = float(row["longitude"])
            a.save()


