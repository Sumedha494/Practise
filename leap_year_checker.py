#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Method 1
try:
    year = int(input("Enter a year to check: "))

    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(f"✅ {year} is a Leap Year!")
    else:
        print(f"❌ {year} is NOT a Leap Year.")

except ValueError:
    print("Please enter a valid number (e.g., 2024).")


# In[ ]:


#Method 2
def is_leap_year(year):
    """
    Returns True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# In[ ]:


years_to_check = [2000, 2023, 2024, 2100]

for y in years_to_check:
    if is_leap_year(y):
        print(f"{y}: Leap Year")
    else:
        print(f"{y}: Not Leap Year")


# In[ ]:


#Method 3
import calendar

year = 2024 

if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

