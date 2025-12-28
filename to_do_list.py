#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tasks = []


# In[ ]:


def display_menu():
    print("\n" + "="*40)
    print("         TO-DO LIST APPLICATION")
    print("="*40)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("="*40)


# In[ ]:


def view_tasks():
    if not tasks:
        print("\n📭 No tasks in your list!")
    else:
        print("\n📋 Your Tasks:")
        print("-" * 40)
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. [{status}] {task['title']}")
        print("-" * 40)


# In[ ]:


def add_task():
    title = input("\nEnter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"✅ Task '{title}' added successfully!")
    else:
        print("❌ Task title cannot be empty!")


# In[ ]:


def mark_complete():
    view_tasks()
    if tasks:
        try:
            index = int(input("\nEnter task number to mark complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print(f"✅ Task '{tasks[index]['title']}' marked as complete!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")


# In[ ]:


def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"🗑️ Task '{removed['title']}' deleted!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")


# In[ ]:


while True:
    display_menu()
    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\n👋 Goodbye! Have a productive day!")
        break
    else:
        print("❌ Invalid choice! Please try again.")

