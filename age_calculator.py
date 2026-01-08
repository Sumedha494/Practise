#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, date


# In[3]:


birth_date = input("Enter your birth date (DD-MM-YYYY): ")

birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()

print(f"✅ Birth Date: {birth_date.strftime('%d %B, %Y')}")


# In[4]:


today = date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

print("🎂 Your Age:")
print(f"   📅 {years} Years, {months} Months, {days} Days")


# In[5]:


total_days = (today - birth_date).days

print(f"📊 Total Days Lived: {total_days:,} days")
print(f"📊 Total Weeks Lived: {total_days // 7:,} weeks")
print(f"📊 Total Months Lived: {total_days // 30:,} months")


# In[6]:


next_birthday = date(today.year, birth_date.month, birth_date.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

days_until_birthday = (next_birthday - today).days

if days_until_birthday == 0:
    print("🎉 Happy Birthday! Today is your birthday!")
else:
    print(f"🎈 Next Birthday: {next_birthday.strftime('%d %B, %Y')}")
    print(f"⏳ Days until birthday: {days_until_birthday} days")

