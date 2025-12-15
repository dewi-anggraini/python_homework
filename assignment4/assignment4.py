import pandas as pd
import numpy as np

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# 1. Create a DataFrame from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print("Data Frame:")
print(task1_data_frame)

# 2. Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000] # add column Salary
print("\nTask 1 With Salary:")
print(task1_with_salary)

# 3. Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older ['Age'] = task1_older ['Age'] + 1 # add column Age with increment age by 1
print("\nTask 1 Older (Age + 1):")
print(task1_older)

# 4. Save the DataFrame as a CSV file:
task1_older.to_csv('employees.csv', index=False) # save data and exclude index
print("\nSaved task1_older DataFrame to employees.csv")

# Task 2:  Loading Data from CSV and JSON

# 1. Read data from a CSV file:
task2_employees = pd.read_csv("employees.csv")
print("\nLoad csv DataFrame:")
print(task2_employees)

# 2. Read data from a JSON file:
[
    {
     "Name": "Eve", 
     "Age": 28, 
     "City": "Miami", 
     "Salary": 60000
     },
    {
     "Name": "Frank", 
     "Age": 40, 
     "City": "Seattle", 
     "Salary": 950000
     }
]
with open("additional_employees.json") as f:
    print("FILE CONTENTS:")
    print(f.read())
    
json_employees = pd.read_json("additional_employees.json")
print("\nLoad JSON DataFRame:")
print(json_employees)

# 3. Combine DataFRame:
more_employees = pd.concat([task2_employees, json_employees], ignore_index= True)
print("\nCombined DataFrame:")
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# 1. Use the head() method on a first 3 row:
first_three = more_employees.head(3)
print("\nFirst 3 rows:")
print(first_three)

# 2. Use the tail() method on the last 2:
last_two = more_employees.tail(2)
print("\nLast two:")
print(last_two)

# 3. Get the shape of a DataFrame
employee_shape = more_employees.shape
print("\nShaped DataFrame:")
print(employee_shape)

# 4. Use the info() method
summary = more_employees.info()
print("\nSummary of DataFrame:")
print(summary)

# Task 4: Data Cleaning
# 1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')
print("\nDirty data:")
print(dirty_data)

# create a copy using copy() method
clean_data = dirty_data.copy()

# 2. Remove any duplicate
clean_data = clean_data.drop_duplicates()
print("\nClean data after removing duplicates:")
print(clean_data)

# 3. Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\nConnverted age:")
print(clean_data)

# 4. Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\nConverted Salary:")
print(clean_data)

#print(type(clean_data))
#print(clean_data.columns.tolist())

# 5.Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data)

# 6. Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(pd.Timestamp("2025-01-01"))
print("\nConverted Hire Date to datetime:")
print(clean_data)

# 7. Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.upper().str.strip()
clean_data["Department"] = clean_data["Department"].str.upper().str.strip()
print(clean_data)
