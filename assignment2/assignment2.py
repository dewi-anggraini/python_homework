import csv
import traceback
import os
import custom_module
from datetime import datetime

# Global variable 
employees = {}
employee_id_column = None
minutes1 = {}
minutes2 = {}
minutes_set = set()
minutes_list = []

# Task 2: Read a CSV file
def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
            data["rows"] = rows
            return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

# load and print the employees
employees = read_employees()
print(employees)

# Task 3: Finf the column index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the employee first name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

# Task 5: Finf the employee: a function in a function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the employee with a lambda
def employee_find_2(employee_id):
   return list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))

# Task 7: Sort the rows by last_name using lambda
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[index])
    return employees["rows"]
# call and print
sort_by_last_name()
print(employees)

# Task 8: Create a dict for an employee
def employee_dict(row):
    return {key: value for key, value in zip(employees["fields"], row) if key != "employee_id"}
# call with valid row
print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, of all employees
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}

print(all_employees_dict())

# Task 10: Use the os module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating your own module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("no_secret")
print(custom_module.secret)

# Task 12: Read minut1.csv and minute2.csv
def read_minutes(): # Main function
    def read_csv_to_dict(path): # Helper function to read a csv file and turns it into a dict
        fields = {}
        rows = []
        with open(path, newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0: # if i = 0 then it saves as the header
                    fields["fields"] = row # header
                else: #if i > 0 add to data row
                    rows.append(tuple(row)) # data row
        fields["rows"] = rows
        return fields
                
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes set
def create_minutes_set():
    global minutes_set
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    minutes_set = set1.union(set2)
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    #global minutes_list
    minutes_list = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write out sorted list
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    # convert datetime → formatted string 
    convert = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    # write to csv
    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in convert:
            writer.writerow(row)
    return convert

print(write_sorted_list())







   





