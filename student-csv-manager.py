#Question:Program to write and read CSV data and compute total and average marks per student.
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "subject", "marks"])
    
    writer.writeheader()
    writer.writerow({"name": "Priya", "subject": "English", "marks": 50})
    writer.writerow({"name": "Priya", "subject": "Maths", "marks": 45})
    writer.writerow({"name": "Vinay", "subject": "English", "marks": 45})
    writer.writerow({"name": "Vinay", "subject": "Maths", "marks": 40})
import csv

totals = {}
counts = {}

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        marks = int(row["marks"])

        if name in totals:
            totals[name] += marks
            counts[name] += 1
        else:
            totals[name] = marks
            counts[name] = 1

for name in totals:
    total = totals[name]
    average = total / counts[name]
    print(name, "Total =", total, "Average =", average)
