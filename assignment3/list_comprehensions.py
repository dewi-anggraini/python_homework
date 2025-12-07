# Task 3: List Comprehensions Practice
import csv
# read csv file
with open("/csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

# create list of name and skip header row
employee_names = [f"{row[0]} {row[1]}" for row in data[1:] ]
print("All employee names: ", employee_names)

# sorting names coontaining 'e'
names_with_e = [name for name in employee_names if 'e' in name.lower()]
print("Names with e: ", names_with_e)
