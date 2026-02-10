#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sample_data = """name,age,city,salary
Rahul,25,Delhi,50000
Priya,22,Mumbai,45000
Amit,28,Bangalore,60000
Sneha,24,Chennai,55000
Vikram,30,Kolkata,70000"""

with open('employees.csv', 'w') as f:
    f.write(sample_data)

print("✅ employees.csv file created!")


# In[ ]:


import csv

with open('employees.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# In[ ]:


import csv

with open('employees.csv', 'r') as file:
    reader = csv.reader(file)

    header = next(reader)
    print(f"📋 Headers: {header}")
    print("-" * 40)

    for row in reader:
        print(f"👤 {row[0]}, Age: {row[1]}, City: {row[2]}")


# In[ ]:


import csv

with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)

    print("📊 Employee Details:")
    print("=" * 50)

    for row in reader:
        print(f"Name: {row['name']}")
        print(f"Age: {row['age']}")
        print(f"City: {row['city']}")
        print(f"Salary: ₹{row['salary']}")
        print("-" * 30)


# In[ ]:


import pandas as pd

df = pd.read_csv('employees.csv')

print("📊 DataFrame:")
print(df)


# In[ ]:


import pandas as pd

df = pd.read_csv('employees.csv')

print("📋 Basic Info:")
print(f"Shape: {df.shape}")  # (rows, columns)
print(f"Columns: {list(df.columns)}")

print("\n📊 First 3 rows:")
print(df.head(3))

print("\n📈 Statistics:")
print(df.describe())

print("\n💰 Total Salary:")
print(f"₹{df['salary'].sum()}")

print("\n📊 Average Age:")
print(f"{df['age'].mean():.1f} years")


# In[ ]:


import pandas as pd

df = pd.read_csv('employees.csv', usecols=['name', 'salary'])

print("📊 Name and Salary Only:")
print(df)


# In[ ]:


import pandas as pd

df = pd.read_csv('employees.csv')

print("👤 Employees with Age > 25:")
filtered = df[df['age'] > 25]
print(filtered)

print("\n💰 Employees with Salary >= 55000:")
high_salary = df[df['salary'] >= 55000]
print(high_salary)

print("\n🏙️ Employees from Delhi:")
delhi_emp = df[df['city'] == 'Delhi']
print(delhi_emp)


# In[ ]:


sample_semicolon = """name;age;city
Rahul;25;Delhi
Priya;22;Mumbai"""

with open('data_semicolon.csv', 'w') as f:
    f.write(sample_semicolon)

import csv

# Method 1: csv module
with open('data_semicolon.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

# Method 2: pandas
import pandas as pd
df = pd.read_csv('data_semicolon.csv', sep=';')
print(df)


# In[ ]:


sample_missing = """name,age,city,salary
Rahul,25,Delhi,50000
Priya,,Mumbai,45000
Amit,28,,60000
Sneha,24,Chennai,
Vikram,30,Kolkata,70000"""

with open('missing_data.csv', 'w') as f:
    f.write(sample_missing)

import pandas as pd

# Read with missing values
df = pd.read_csv('missing_data.csv')

print("📊 Data with Missing Values:")
print(df)

print("\n❓ Check Missing Values:")
print(df.isnull().sum())

df_filled = df.fillna({
    'age': df['age'].mean(),
    'city': 'Unknown',
    'salary': 0
})

print("\n✅ After Filling Missing Values:")
print(df_filled)


# In[ ]:


import pandas as pd

# Large file ko chunks mein read karna
chunk_size = 2

print("📊 Reading in Chunks:")
print("=" * 40)

for i, chunk in enumerate(pd.read_csv('employees.csv', chunksize=chunk_size)):
    print(f"\n📦 Chunk {i + 1}:")
    print(chunk)


# In[ ]:


import pandas as pd

# Online CSV file read karna
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"

try:
    df = pd.read_csv(url)
    print("📊 Online CSV Data:")
    print(df.head())
except Exception as e:
    print(f"❌ Error: {e}")


# In[ ]:


import csv

with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Convert to list of dictionaries
    data = list(reader)

print("📊 List of Dictionaries:")
for emp in data:
    print(emp)

# Access specific record
print(f"\n👤 First Employee: {data[0]['name']}")


# In[ ]:


import csv
import pandas as pd

class CSVReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read_basic(self):
        """Basic CSV reading"""
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def read_as_dict(self):
        """Read as list of dictionaries"""
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def read_pandas(self):
        """Read using pandas"""
        self.data = pd.read_csv(self.filename)
        return self.data

    def get_column(self, column_name):
        """Get specific column"""
        if self.data is None:
            self.read_pandas()
        return self.data[column_name].tolist()

    def filter_data(self, column, value):
        """Filter data by column value"""
        if self.data is None:
            self.read_pandas()
        return self.data[self.data[column] == value]

    def summary(self):
        """Print summary of CSV"""
        if self.data is None:
            self.read_pandas()

        print("=" * 45)
        print("📊 CSV FILE SUMMARY")
        print("=" * 45)
        print(f"📁 File: {self.filename}")
        print(f"📏 Rows: {len(self.data)}")
        print(f"📐 Columns: {len(self.data.columns)}")
        print(f"📋 Column Names: {list(self.data.columns)}")
        print("\n📊 Data Preview:")
        print(self.data.head())
        print("=" * 45)

# Usage
reader = CSVReader('employees.csv')
reader.summary()

print("\n💰 Salaries:")
print(reader.get_column('salary'))

print("\n🏙️ Delhi Employees:")
print(reader.filter_data('city', 'Delhi'))


# In[ ]:


import pandas as pd

encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']

for encoding in encodings:
    try:
        df = pd.read_csv('employees.csv', encoding=encoding)
        print(f"✅ Success with encoding: {encoding}")
        break
    except Exception as e:
        print(f"❌ Failed with {encoding}: {e}")


# In[ ]:


import pandas as pd

# Custom column names dena
custom_headers = ['Employee_Name', 'Employee_Age', 'Employee_City', 'Employee_Salary']

df = pd.read_csv('employees.csv', 
                  header=0,  # First row is header (skip it)
                  names=custom_headers,
                  skiprows=1)  # Skip original header

print("📊 With Custom Headers:")
print(df)


# In[ ]:


import pandas as pd
import csv

def interactive_csv_reader():
    while True:
        print("\n📄 CSV READER MENU")
        print("=" * 35)
        print("1. Read & Display CSV")
        print("2. Show Column Names")
        print("3. Show Specific Column")
        print("4. Filter Data")
        print("5. Basic Statistics")
        print("6. Search Value")
        print("7. Export Filtered Data")
        print("8. Exit")

        choice = input("\nChoice (1-8): ")

        if choice == '8':
            print("Goodbye! 👋")
            break

        filename = input("Enter CSV filename: ")

        try:
            df = pd.read_csv(filename)

            if choice == '1':
                print(f"\n📊 Data from {filename}:")
                print(df)

            elif choice == '2':
                print(f"\n📋 Columns: {list(df.columns)}")

            elif choice == '3':
                col = input("Enter column name: ")
                if col in df.columns:
                    print(f"\n📊 {col}:")
                    print(df[col])
                else:
                    print("❌ Column not found!")

            elif choice == '4':
                col = input("Filter by column: ")
                val = input("Filter value: ")
                filtered = df[df[col].astype(str) == val]
                print(f"\n📊 Filtered Data:")
                print(filtered)

            elif choice == '5':
                print(f"\n📈 Statistics:")
                print(df.describe())

            elif choice == '6':
                search = input("Search value: ")
                mask = df.apply(lambda x: x.astype(str).str.contains(search, case=False)).any(axis=1)
                print(f"\n🔍 Search Results:")
                print(df[mask])

            elif choice == '7':
                col = input("Filter by column: ")
                val = input("Filter value: ")
                filtered = df[df[col].astype(str) == val]
                output_file = input("Output filename: ")
                filtered.to_csv(output_file, index=False)
                print(f"✅ Saved to {output_file}")

        except FileNotFoundError:
            print(f"❌ File '{filename}' not found!")
        except Exception as e:
            print(f"❌ Error: {e}")


