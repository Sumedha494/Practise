#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Simple Student Performance Calculator

def calculate_percentage(marks):
    """Calculate percentage from marks"""
    total = sum(marks)
    max_marks = len(marks) * 100
    percentage = (total / max_marks) * 100
    return round(percentage, 2)

def get_grade(percentage):
    """Get grade based on percentage"""
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    elif percentage >= 35:
        return 'E'
    else:
        return 'F'

def analyze_student(name, marks):
    """Analyze single student performance"""
    percentage = calculate_percentage(marks)
    grade = get_grade(percentage)
    total = sum(marks)
    average = total / len(marks)
    status = "PASS" if percentage >= 35 else "FAIL"

    print("\n" + "=" * 40)
    print(f"📊 STUDENT PERFORMANCE REPORT")
    print("=" * 40)
    print(f"👤 Name: {name}")
    print(f"📝 Marks: {marks}")
    print(f"📈 Total: {total}/{len(marks)*100}")
    print(f"📊 Percentage: {percentage}%")
    print(f"📉 Average: {average:.2f}")
    print(f"🎓 Grade: {grade}")
    print(f"✅ Status: {status}")
    print("=" * 40)

# Example
name = input("Enter student name: ")
subjects = int(input("How many subjects? "))

marks = []
for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

analyze_student(name, marks)


# In[2]:


def student_performance_analyzer():
    """Analyze multiple students"""

    students = {}
    subjects = ['Math', 'Science', 'English', 'Hindi', 'Computer']

    def add_student():
        name = input("\n👤 Enter student name: ")
        marks = {}

        print(f"Enter marks for {name}:")
        for subject in subjects:
            while True:
                try:
                    mark = int(input(f"  {subject}: "))
                    if 0 <= mark <= 100:
                        marks[subject] = mark
                        break
                    else:
                        print("  ❌ Enter marks between 0-100!")
                except ValueError:
                    print("  ❌ Enter a valid number!")

        students[name] = marks
        print(f"✅ {name} added successfully!")

    def calculate_stats(marks):
        total = sum(marks.values())
        percentage = (total / (len(marks) * 100)) * 100
        average = total / len(marks)

        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        elif percentage >= 35:
            grade = 'E'
        else:
            grade = 'F'

        status = "PASS" if percentage >= 35 else "FAIL"

        return {
            'total': total,
            'percentage': round(percentage, 2),
            'average': round(average, 2),
            'grade': grade,
            'status': status,
            'highest': max(marks.values()),
            'lowest': min(marks.values())
        }

    def show_all_students():
        if not students:
            print("\n❌ No students added yet!")
            return

        print("\n" + "╔" + "═" * 70 + "╗")
        print("║" + "📊 ALL STUDENTS PERFORMANCE".center(70) + "║")
        print("╠" + "═" * 70 + "╣")
        print(f"║  {'Name':<12}│{'Total':>7}│{'%':>8}│{'Grade':>6}│{'Status':>8}│{'Rank':>6}  ║")
        print("╠" + "═" * 70 + "╣")

        # Calculate rankings
        rankings = []
        for name, marks in students.items():
            stats = calculate_stats(marks)
            rankings.append((name, stats))

        # Sort by percentage
        rankings.sort(key=lambda x: x[1]['percentage'], reverse=True)

        for rank, (name, stats) in enumerate(rankings, 1):
            status_icon = "✅" if stats['status'] == "PASS" else "❌"
            print(f"║  {name:<12}│{stats['total']:>7}│{stats['percentage']:>7}%│{stats['grade']:>6}│{status_icon} {stats['status']:<5}│{rank:>6}  ║")

        print("╚" + "═" * 70 + "╝")

    def show_student_detail(name):
        if name not in students:
            print(f"❌ Student '{name}' not found!")
            return

        marks = students[name]
        stats = calculate_stats(marks)

        print("\n" + "╔" + "═" * 50 + "╗")
        print(f"║  📊 DETAILED REPORT - {name.upper()}".ljust(51) + "║")
        print("╠" + "═" * 50 + "╣")
        print("║  📚 SUBJECT-WISE MARKS:".ljust(51) + "║")

        for subject, mark in marks.items():
            bar = "█" * (mark // 5) + "░" * (20 - mark // 5)
            status = "✅" if mark >= 35 else "❌"
            print(f"║  {subject:<10}: {mark:>3} │{bar}│ {status}".ljust(51) + "║")

        print("╠" + "═" * 50 + "╣")
        print(f"║  📈 Total        : {stats['total']}/500".ljust(51) + "║")
        print(f"║  📊 Percentage   : {stats['percentage']}%".ljust(51) + "║")
        print(f"║  📉 Average      : {stats['average']}".ljust(51) + "║")
        print(f"║  🎓 Grade        : {stats['grade']}".ljust(51) + "║")
        print(f"║  ⬆️  Highest      : {stats['highest']}".ljust(51) + "║")
        print(f"║  ⬇️  Lowest       : {stats['lowest']}".ljust(51) + "║")
        print(f"║  ✅ Status       : {stats['status']}".ljust(51) + "║")
        print("╚" + "═" * 50 + "╝")

    def subject_analysis():
        if not students:
            print("\n❌ No students added yet!")
            return

        print("\n" + "╔" + "═" * 55 + "╗")
        print("║" + "📚 SUBJECT-WISE ANALYSIS".center(55) + "║")
        print("╠" + "═" * 55 + "╣")
        print(f"║  {'Subject':<12}│{'Avg':>7}│{'Highest':>8}│{'Lowest':>7}│{'Pass%':>8}  ║")
        print("╠" + "═" * 55 + "╣")

        for subject in subjects:
            marks_list = [students[s][subject] for s in students]
            avg = sum(marks_list) / len(marks_list)
            highest = max(marks_list)
            lowest = min(marks_list)
            pass_count = sum(1 for m in marks_list if m >= 35)
            pass_percent = (pass_count / len(marks_list)) * 100

            print(f"║  {subject:<12}│{avg:>7.1f}│{highest:>8}│{lowest:>7}│{pass_percent:>7.0f}%  ║")

        print("╚" + "═" * 55 + "╝")

    def class_statistics():
        if not students:
            print("\n❌ No students added yet!")
            return

        percentages = []
        grade_count = {'A+': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        pass_count = 0

        for name, marks in students.items():
            stats = calculate_stats(marks)
            percentages.append(stats['percentage'])
            grade_count[stats['grade']] += 1
            if stats['status'] == "PASS":
                pass_count += 1

        class_avg = sum(percentages) / len(percentages)
        pass_percent = (pass_count / len(students)) * 100

        # Find topper
        topper = max(students.keys(), key=lambda x: calculate_stats(students[x])['percentage'])
        topper_percent = calculate_stats(students[topper])['percentage']

        print("\n" + "╔" + "═" * 45 + "╗")
        print("║" + "📊 CLASS STATISTICS".center(45) + "║")
        print("╠" + "═" * 45 + "╣")
        print(f"║  👥 Total Students    : {len(students)}".ljust(46) + "║")
        print(f"║  📊 Class Average     : {class_avg:.2f}%".ljust(46) + "║")
        print(f"║  ⬆️  Highest           : {max(percentages)}%".ljust(46) + "║")
        print(f"║  ⬇️  Lowest            : {min(percentages)}%".ljust(46) + "║")
        print(f"║  ✅ Pass Rate         : {pass_percent:.1f}%".ljust(46) + "║")
        print(f"║  🏆 Topper            : {topper} ({topper_percent}%)".ljust(46) + "║")
        print("╠" + "═" * 45 + "╣")
        print("║  📈 GRADE DISTRIBUTION:".ljust(46) + "║")

        for grade, count in grade_count.items():
            if count > 0:
                bar = "█" * count
                print(f"║     {grade}: {bar} ({count})".ljust(46) + "║")

        print("╚" + "═" * 45 + "╝")

    # Menu
    while True:
        print("\n" + "╔" + "═" * 40 + "╗")
        print("║" + "📊 STUDENT PERFORMANCE ANALYZER".center(40) + "║")
        print("╠" + "═" * 40 + "╣")
        print("║  1. ➕ Add Student                     ║")
        print("║  2. 📋 View All Students               ║")
        print("║  3. 🔍 View Student Details            ║")
        print("║  4. 📚 Subject-wise Analysis           ║")
        print("║  5. 📊 Class Statistics                ║")
        print("║  6. 🚪 Exit                            ║")
        print("╚" + "═" * 40 + "╝")

        choice = input("\n👉 Choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            name = input("Enter student name: ")
            show_student_detail(name)
        elif choice == '4':
            subject_analysis()
        elif choice == '5':
            class_statistics()
        elif choice == '6':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

# Run
student_performance_analyzer()


# In[3]:


import csv
import os
from datetime import datetime

class StudentDatabase:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.subjects = ['Math', 'Science', 'English', 'Hindi', 'Computer']
        self.load_data()

    def load_data(self):
        """Load data from CSV file"""
        self.students = {}

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    marks = {subj: int(row[subj]) for subj in self.subjects}
                    self.students[name] = marks
            print(f"✅ Loaded {len(self.students)} students from {self.filename}")

    def save_data(self):
        """Save data to CSV file"""
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['Name'] + self.subjects
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for name, marks in self.students.items():
                row = {'Name': name}
                row.update(marks)
                writer.writerow(row)

        print(f"✅ Data saved to {self.filename}")

    def add_student(self, name, marks):
        """Add new student"""
        self.students[name] = marks
        self.save_data()

    def delete_student(self, name):
        """Delete student"""
        if name in self.students:
            del self.students[name]
            self.save_data()
            return True
        return False

    def update_marks(self, name, subject, marks):
        """Update student marks"""
        if name in self.students and subject in self.subjects:
            self.students[name][subject] = marks
            self.save_data()
            return True
        return False

    def get_student(self, name):
        """Get student data"""
        return self.students.get(name, None)

    def get_all_students(self):
        """Get all students"""
        return self.students

    def export_report(self, filename="report.txt"):
        """Export detailed report"""
        with open(filename, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("STUDENT PERFORMANCE REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")

            for name, marks in self.students.items():
                total = sum(marks.values())
                percentage = (total / 500) * 100

                f.write(f"Student: {name}\n")
                f.write("-" * 30 + "\n")
                for subj, mark in marks.items():
                    f.write(f"  {subj}: {mark}\n")
                f.write(f"  Total: {total}/500\n")
                f.write(f"  Percentage: {percentage:.2f}%\n")
                f.write("\n")

        print(f"✅ Report exported to {filename}")


# Usage Example
db = StudentDatabase()

# Add sample students
sample_data = {
    'Rahul': {'Math': 85, 'Science': 78, 'English': 92, 'Hindi': 88, 'Computer': 95},
    'Priya': {'Math': 92, 'Science': 88, 'English': 85, 'Hindi': 90, 'Computer': 88},
    'Amit': {'Math': 65, 'Science': 70, 'English': 68, 'Hindi': 72, 'Computer': 75},
    'Sneha': {'Math': 78, 'Science': 82, 'English': 80, 'Hindi': 85, 'Computer': 90},
}

for name, marks in sample_data.items():
    db.add_student(name, marks)

print("\n📊 All Students:")
for name, marks in db.get_all_students().items():
    print(f"  {name}: {sum(marks.values())}/500")


# In[4]:


import matplotlib.pyplot as plt
import numpy as np

class PerformanceVisualizer:
    def __init__(self, students_data, subjects):
        self.students = students_data
        self.subjects = subjects

    def bar_chart_comparison(self):
        """Compare students with bar chart"""
        names = list(self.students.keys())
        percentages = []

        for name in names:
            total = sum(self.students[name].values())
            percentage = (total / 500) * 100
            percentages.append(percentage)

        # Colors based on performance
        colors = []
        for p in percentages:
            if p >= 80:
                colors.append('#27ae60')  # Green
            elif p >= 60:
                colors.append('#3498db')  # Blue
            elif p >= 40:
                colors.append('#f39c12')  # Orange
            else:
                colors.append('#e74c3c')  # Red

        plt.figure(figsize=(10, 6))
        bars = plt.bar(names, percentages, color=colors, edgecolor='black')

        # Add value labels
        for bar, pct in zip(bars, percentages):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{pct:.1f}%', ha='center', fontsize=10, fontweight='bold')

        plt.xlabel('Students', fontsize=12)
        plt.ylabel('Percentage (%)', fontsize=12)
        plt.title('📊 Student Performance Comparison', fontsize=14, fontweight='bold')
        plt.ylim(0, 110)
        plt.axhline(y=35, color='red', linestyle='--', label='Pass Line (35%)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('student_comparison.png', dpi=150)
        plt.show()
        print("✅ Chart saved as 'student_comparison.png'")

    def subject_wise_chart(self, student_name):
        """Subject-wise marks for a student"""
        if student_name not in self.students:
            print(f"❌ Student '{student_name}' not found!")
            return

        marks = self.students[student_name]
        subjects = list(marks.keys())
        values = list(marks.values())

        # Colors
        colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']

        plt.figure(figsize=(10, 6))
        bars = plt.bar(subjects, values, color=colors, edgecolor='black')

        # Add value labels
        for bar, val in zip(bars, values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    str(val), ha='center', fontsize=11, fontweight='bold')

        plt.xlabel('Subjects', fontsize=12)
        plt.ylabel('Marks', fontsize=12)
        plt.title(f'📊 Subject-wise Performance - {student_name}', fontsize=14, fontweight='bold')
        plt.ylim(0, 110)
        plt.axhline(y=35, color='red', linestyle='--', label='Pass Marks (35)')
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'{student_name}_subjects.png', dpi=150)
        plt.show()

    def pie_chart_grades(self):
        """Pie chart of grade distribution"""
        grades = {'A+': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}

        for marks in self.students.values():
            total = sum(marks.values())
            percentage = (total / 500) * 100

            if percentage >= 90:
                grades['A+'] += 1
            elif percentage >= 80:
                grades['A'] += 1
            elif percentage >= 70:
                grades['B'] += 1
            elif percentage >= 60:
                grades['C'] += 1
            elif percentage >= 50:
                grades['D'] += 1
            elif percentage >= 35:
                grades['E'] += 1
            else:
                grades['F'] += 1

        # Remove empty grades
        grades = {k: v for k, v in grades.items() if v > 0}

        colors = ['#27ae60', '#2ecc71', '#3498db', '#f39c12', '#e67e22', '#e74c3c', '#c0392b']

        plt.figure(figsize=(8, 8))
        plt.pie(grades.values(), labels=grades.keys(), autopct='%1.1f%%',
                colors=colors[:len(grades)], explode=[0.05]*len(grades),
                shadow=True, startangle=90)
        plt.title('📊 Grade Distribution', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('grade_distribution.png', dpi=150)
        plt.show()

    def subject_average_chart(self):
        """Average marks per subject"""
        subject_totals = {subj: 0 for subj in self.subjects}

        for marks in self.students.values():
            for subj, mark in marks.items():
                subject_totals[subj] += mark

        num_students = len(self.students)
        averages = {subj: total/num_students for subj, total in subject_totals.items()}

        colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']

        plt.figure(figsize=(10, 6))
        bars = plt.bar(averages.keys(), averages.values(), color=colors, edgecolor='black')

        for bar, val in zip(bars, averages.values()):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{val:.1f}', ha='center', fontsize=11, fontweight='bold')

        plt.xlabel('Subjects', fontsize=12)
        plt.ylabel('Average Marks', fontsize=12)
        plt.title('📊 Subject-wise Class Average', fontsize=14, fontweight='bold')
        plt.ylim(0, 110)
        plt.tight_layout()
        plt.savefig('subject_averages.png', dpi=150)
        plt.show()

    def radar_chart(self, student_name):
        """Radar/Spider chart for student"""
        if student_name not in self.students:
            print(f"❌ Student '{student_name}' not found!")
            return

        marks = self.students[student_name]
        subjects = list(marks.keys())
        values = list(marks.values())

        # Number of subjects
        num_vars = len(subjects)

        # Compute angle for each subject
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

        ax.plot(angles, values, 'o-', linewidth=2, color='#3498db')
        ax.fill(angles, values, alpha=0.25, color='#3498db')

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(subjects, fontsize=11)
        ax.set_ylim(0, 100)

        plt.title(f'📊 Performance Radar - {student_name}', fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig(f'{student_name}_radar.png', dpi=150)
        plt.show()

    def trend_line(self, student_name, exam_history):
        """Performance trend over multiple exams"""
        exams = list(exam_history.keys())
        percentages = list(exam_history.values())

        plt.figure(figsize=(10, 6))
        plt.plot(exams, percentages, 'bo-', linewidth=2, markersize=10)
        plt.fill_between(exams, percentages, alpha=0.3)

        for i, pct in enumerate(percentages):
            plt.annotate(f'{pct}%', (exams[i], pct), textcoords="offset points",
                        xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')

        plt.xlabel('Exams', fontsize=12)
        plt.ylabel('Percentage (%)', fontsize=12)
        plt.title(f'📈 Performance Trend - {student_name}', fontsize=14, fontweight='bold')
        plt.ylim(0, 100)
        plt.axhline(y=35, color='red', linestyle='--', label='Pass Line')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{student_name}_trend.png', dpi=150)
        plt.show()


# Example Usage
students_data = {
    'Rahul': {'Math': 85, 'Science': 78, 'English': 92, 'Hindi': 88, 'Computer': 95},
    'Priya': {'Math': 92, 'Science': 88, 'English': 85, 'Hindi': 90, 'Computer': 88},
    'Amit': {'Math': 65, 'Science': 70, 'English': 68, 'Hindi': 72, 'Computer': 75},
    'Sneha': {'Math': 78, 'Science': 82, 'English': 80, 'Hindi': 85, 'Computer': 90},
    'Vikram': {'Math': 45, 'Science': 52, 'English': 48, 'Hindi': 55, 'Computer': 60},
}

subjects = ['Math', 'Science', 'English', 'Hindi', 'Computer']

viz = PerformanceVisualizer(students_data, subjects)

# Generate charts
viz.bar_chart_comparison()
viz.subject_wise_chart('Rahul')
viz.pie_chart_grades()
viz.subject_average_chart()
viz.radar_chart('Priya')

# Trend example
exam_history = {
    'Unit 1': 65,
    'Unit 2': 72,
    'Mid Term': 78,
    'Unit 3': 82,
    'Final': 88
}
viz.trend_line('Rahul', exam_history)


# In[5]:


import os
import csv
from datetime import datetime

class Student:
    """Student class to store individual student data"""

    def __init__(self, roll_no, name, class_name, marks=None):
        self.roll_no = roll_no
        self.name = name
        self.class_name = class_name
        self.marks = marks if marks else {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def get_total(self):
        return sum(self.marks.values())

    def get_percentage(self):
        if not self.marks:
            return 0
        max_marks = len(self.marks) * 100
        return round((self.get_total() / max_marks) * 100, 2)

    def get_grade(self):
        percentage = self.get_percentage()
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B'
        elif percentage >= 60:
            return 'C'
        elif percentage >= 50:
            return 'D'
        elif percentage >= 35:
            return 'E'
        else:
            return 'F'

    def get_status(self):
        # Check if failed in any subject
        for mark in self.marks.values():
            if mark < 35:
                return "FAIL"
        return "PASS" if self.get_percentage() >= 35 else "FAIL"

    def get_average(self):
        if not self.marks:
            return 0
        return round(self.get_total() / len(self.marks), 2)

    def get_highest_subject(self):
        if not self.marks:
            return None, 0
        subject = max(self.marks, key=self.marks.get)
        return subject, self.marks[subject]

    def get_lowest_subject(self):
        if not self.marks:
            return None, 0
        subject = min(self.marks, key=self.marks.get)
        return subject, self.marks[subject]

    def get_failed_subjects(self):
        return [subj for subj, mark in self.marks.items() if mark < 35]


class StudentPerformanceAnalyzer:
    """Main analyzer class"""

    def __init__(self):
        self.students = {}
        self.subjects = ['Mathematics', 'Science', 'English', 'Hindi', 'Computer']
        self.filename = "student_data.csv"
        self.load_data()

    def load_data(self):
        """Load data from CSV"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        roll_no = row['Roll_No']
                        name = row['Name']
                        class_name = row['Class']
                        marks = {subj: int(row[subj]) for subj in self.subjects if subj in row}

                        student = Student(roll_no, name, class_name, marks)
                        self.students[roll_no] = student

                print(f"✅ Loaded {len(self.students)} students")
            except Exception as e:
                print(f"⚠️ Error loading data: {e}")

    def save_data(self):
        """Save data to CSV"""
        try:
            with open(self.filename, 'w', newline='') as file:
                fieldnames = ['Roll_No', 'Name', 'Class'] + self.subjects
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                for roll_no, student in self.students.items():
                    row = {
                        'Roll_No': student.roll_no,
                        'Name': student.name,
                        'Class': student.class_name
                    }
                    row.update(student.marks)
                    writer.writerow(row)

            print(f"✅ Data saved successfully!")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def add_student(self):
        """Add new student"""
        print("\n➕ ADD NEW STUDENT")
        print("-" * 30)

        roll_no = input("Roll Number: ")

        if roll_no in self.students:
            print("❌ Roll number already exists!")
            return

        name = input("Name: ")
        class_name = input("Class: ")

        student = Student(roll_no, name, class_name)

        print(f"\nEnter marks for {name}:")
        for subject in self.subjects:
            while True:
                try:
                    mark = int(input(f"  {subject}: "))
                    if 0 <= mark <= 100:
                        student.add_marks(subject, mark)
                        break
                    else:
                        print("  ❌ Enter marks between 0-100!")
                except ValueError:
                    print("  ❌ Enter a valid number!")

        self.students[roll_no] = student
        self.save_data()
        print(f"\n✅ {name} added successfully!")

    def update_student(self):
        """Update student marks"""
        roll_no = input("\nEnter Roll Number to update: ")

        if roll_no not in self.students:
            print("❌ Student not found!")
            return

        student = self.students[roll_no]
        print(f"\n📝 Updating marks for {student.name}")
        print("Current marks:", student.marks)

        print("\nEnter new marks (press Enter to keep current):")
        for subject in self.subjects:
            current = student.marks.get(subject, 0)
            new_mark = input(f"  {subject} [{current}]: ")

            if new_mark:
                try:
                    mark = int(new_mark)
                    if 0 <= mark <= 100:
                        student.marks[subject] = mark
                except ValueError:
                    print(f"  ⚠️ Invalid input, keeping {current}")

        self.save_data()
        print("✅ Marks updated!")

    def delete_student(self):
        """Delete student"""
        roll_no = input("\nEnter Roll Number to delete: ")

        if roll_no not in self.students:
            print("❌ Student not found!")
            return

        name = self.students[roll_no].name
        confirm = input(f"Delete {name}? (y/n): ").lower()

        if confirm == 'y':
            del self.students[roll_no]
            self.save_data()
            print(f"✅ {name} deleted!")

    def view_all_students(self):
        """View all students"""
        if not self.students:
            print("\n❌ No students found!")
            return

        # Sort by percentage
        sorted_students = sorted(
            self.students.values(),
            key=lambda s: s.get_percentage(),
            reverse=True
        )

        print("\n" + "╔" + "═" * 80 + "╗")
        print("║" + "📊 ALL STUDENTS PERFORMANCE".center(80) + "║")
        print("╠" + "═" * 80 + "╣")
        print(f"║  {'Rank':<5}{'Roll':<8}{'Name':<15}{'Class':<8}{'Total':<8}{'%':<8}{'Grade':<7}{'Status':<8}║")
        print("╠" + "═" * 80 + "╣")

        for rank, student in enumerate(sorted_students, 1):
            status_icon = "✅" if student.get_status() == "PASS" else "❌"
            total = f"{student.get_total()}/{len(self.subjects)*100}"

            print(f"║  {rank:<5}{student.roll_no:<8}{student.name:<15}{student.class_name:<8}"
                  f"{total:<8}{student.get_percentage():<7}%{student.get_grade():<7}"
                  f"{status_icon} {student.get_status():<5}║")

        print("╚" + "═" * 80 + "╝")
        print(f"\n📊 Total Students: {len(self.students)}")

    def view_student_detail(self):
        """View detailed student report"""
        roll_no = input("\nEnter Roll Number: ")

        if roll_no not in self.students:
            print("❌ Student not found!")
            return

        student = self.students[roll_no]
        highest = student.get_highest_subject()
        lowest = student.get_lowest_subject()
        failed = student.get_failed_subjects()

        print("\n" + "╔" + "═" * 55 + "╗")
        print(f"║  📊 DETAILED REPORT".ljust(56) + "║")
        print("╠" + "═" * 55 + "╣")
        print(f"║  🆔 Roll Number : {student.roll_no}".ljust(56) + "║")
        print(f"║  👤 Name        : {student.name}".ljust(56) + "║")
        print(f"║  🏫 Class       : {student.class_name}".ljust(56) + "║")
        print("╠" + "═" * 55 + "╣")
        print("║  📚 SUBJECT-WISE MARKS:".ljust(56) + "║")

        for subject, mark in student.marks.items():
            # Progress bar
            bar_length = 20
            filled = int((mark / 100) * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            status = "✅" if mark >= 35 else "❌"

            print(f"║  {subject:<12}: {mark:>3} │{bar}│ {status}".ljust(56) + "║")

        print("╠" + "═" * 55 + "╣")
        print(f"║  📈 Total        : {student.get_total()}/{len(self.subjects)*100}".ljust(56) + "║")
        print(f"║  📊 Percentage   : {student.get_percentage()}%".ljust(56) + "║")
        print(f"║  📉 Average      : {student.get_average()}".ljust(56) + "║")
        print(f"║  🎓 Grade        : {student.get_grade()}".ljust(56) + "║")
        print(f"║  ⬆️  Best Subject : {highest[0]} ({highest[1]})".ljust(56) + "║")
        print(f"║  ⬇️  Weak Subject : {lowest[0]} ({lowest[1]})".ljust(56) + "║")

        if failed:
            print(f"║  ❌ Failed In    : {', '.join(failed)}".ljust(56) + "║")

        print(f"║  ✅ Status       : {student.get_status()}".ljust(56) + "║")
        print("╚" + "═" * 55 + "╝")

    def subject_analysis(self):
        """Subject-wise analysis"""
        if not self.students:
            print("\n❌ No students found!")
            return

        print("\n" + "╔" + "═" * 65 + "╗")
        print("║" + "📚 SUBJECT-WISE ANALYSIS".center(65) + "║")
        print("╠" + "═" * 65 + "╣")
        print(f"║  {'Subject':<15}│{'Avg':>8}│{'Highest':>9}│{'Lowest':>8}│{'Pass':>8}│{'Fail':>8}║")
        print("╠" + "═" * 65 + "╣")

        for subject in self.subjects:
            marks = [s.marks.get(subject, 0) for s in self.students.values()]

            avg = sum(marks) / len(marks)
            highest = max(marks)
            lowest = min(marks)
            pass_count = sum(1 for m in marks if m >= 35)
            fail_count = len(marks) - pass_count

            print(f"║  {subject:<15}│{avg:>7.1f}│{highest:>9}│{lowest:>8}│{pass_count:>8}│{fail_count:>8}║")

        print("╚" + "═" * 65 + "╝")

    def class_statistics(self):
        """Overall class statistics"""
        if not self.students:
            print("\n❌ No students found!")
            return

        percentages = [s.get_percentage() for s in self.students.values()]
        grades = {}
        pass_count = 0

        for student in self.students.values():
            grade = student.get_grade()
            grades[grade] = grades.get(grade, 0) + 1
            if student.get_status() == "PASS":
                pass_count += 1

        # Find topper
        topper = max(self.students.values(), key=lambda s: s.get_percentage())

        print("\n" + "╔" + "═" * 50 + "╗")
        print("║" + "📊 CLASS STATISTICS".center(50) + "║")
        print("╠" + "═" * 50 + "╣")
        print(f"║  👥 Total Students    : {len(self.students)}".ljust(51) + "║")
        print(f"║  📊 Class Average     : {sum(percentages)/len(percentages):.2f}%".ljust(51) + "║")
        print(f"║  ⬆️  Highest Score     : {max(percentages)}%".ljust(51) + "║")
        print(f"║  ⬇️  Lowest Score      : {min(percentages)}%".ljust(51) + "║")
        print(f"║  ✅ Pass Count        : {pass_count}".ljust(51) + "║")
        print(f"║  ❌ Fail Count        : {len(self.students) - pass_count}".ljust(51) + "║")
        print(f"║  📈 Pass Rate         : {(pass_count/len(self.students))*100:.1f}%".ljust(51) + "║")
        print(f"║  🏆 Topper            : {topper.name} ({topper.get_percentage()}%)".ljust(51) + "║")
        print("╠" + "═" * 50 + "╣")
        print("║  📈 GRADE DISTRIBUTION:".ljust(51) + "║")

        for grade in ['A+', 'A', 'B', 'C', 'D', 'E', 'F']:
            count = grades.get(grade, 0)
            if count > 0:
                bar = "█" * count
                print(f"║     {grade}: {bar} ({count})".ljust(51) + "║")

        print("╚" + "═" * 50 + "╝")

    def top_performers(self):
        """Show top 5 performers"""
        if not self.students:
            print("\n❌ No students found!")
            return

        sorted_students = sorted(
            self.students.values(),
            key=lambda s: s.get_percentage(),
            reverse=True
        )[:5]

        print("\n" + "╔" + "═" * 50 + "╗")
        print("║" + "🏆 TOP 5 PERFORMERS".center(50) + "║")
        print("╠" + "═" * 50 + "╣")

        medals = ['🥇', '🥈', '🥉', '4️⃣', '5️⃣']

        for i, student in enumerate(sorted_students):
            print(f"║  {medals[i]} {student.name:<20} │ {student.get_percentage()}% │ {student.get_grade()}".ljust(51) + "║")

        print("╚" + "═" * 50 + "╝")

    def failed_students(self):
        """Show failed students"""
        failed = [s for s in self.students.values() if s.get_status() == "FAIL"]

        if not failed:
            print("\n✅ No failed students!")
            return

        print("\n" + "╔" + "═" * 55 + "╗")
        print("║" + "❌ FAILED STUDENTS".center(55) + "║")
        print("╠" + "═" * 55 + "╣")

        for student in failed:
            failed_subjects = student.get_failed_subjects()
            print(f"║  👤 {student.name:<15} │ {student.get_percentage()}%".ljust(56) + "║")
            print(f"║     Failed in: {', '.join(failed_subjects)}".ljust(56) + "║")
            print("║" + "-" * 55 + "║")

        print("╚" + "═" * 55 + "╝")

    def search_student(self):
        """Search student by name"""
        query = input("\nEnter name to search: ").lower()

        results = [s for s in self.students.values() if query in s.name.lower()]

        if not results:
            print("❌ No students found!")
            return

        print(f"\n📊 Found {len(results)} student(s):")
        for student in results:
            print(f"  [{student.roll_no}] {student.name} - {student.get_percentage()}% ({student.get_grade()})")

    def export_report(self):
        """Export detailed report to file"""
        filename = f"performance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("STUDENT PERFORMANCE REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")

            # Sort by percentage
            sorted_students = sorted(
                self.students.values(),
                key=lambda s: s.get_percentage(),
                reverse=True
            )

            for rank, student in enumerate(sorted_students, 1):
                f.write(f"Rank #{rank}\n")
                f.write("-" * 40 + "\n")
                f.write(f"Roll No: {student.roll_no}\n")
                f.write(f"Name: {student.name}\n")
                f.write(f"Class: {student.class_name}\n")
                f.write("\nSubject-wise Marks:\n")

                for subject, mark in student.marks.items():
                    status = "PASS" if mark >= 35 else "FAIL"
                    f.write(f"  {subject}: {mark} ({status})\n")

                f.write(f"\nTotal: {student.get_total()}/{len(self.subjects)*100}\n")
                f.write(f"Percentage: {student.get_percentage()}%\n")
                f.write(f"Grade: {student.get_grade()}\n")
                f.write(f"Status: {student.get_status()}\n")
                f.write("\n" + "=" * 40 + "\n\n")

            # Summary
            f.write("\nCLASS SUMMARY\n")
            f.write("-" * 40 + "\n")
            percentages = [s.get_percentage() for s in self.students.values()]
            pass_count = sum(1 for s in self.students.values() if s.get_status() == "PASS")

            f.write(f"Total Students: {len(self.students)}\n")
            f.write(f"Class Average: {sum(percentages)/len(percentages):.2f}%\n")
            f.write(f"Pass Rate: {(pass_count/len(self.students))*100:.1f}%\n")

        print(f"✅ Report exported to {filename}")

    def show_menu(self):
        """Display main menu"""
        print("\n" + "╔" + "═" * 45 + "╗")
        print("║" + "📊 STUDENT PERFORMANCE ANALYZER".center(45) + "║")
        print("╠" + "═" * 45 + "╣")
        print("║  1.  ➕ Add Student                        ║")
        print("║  2.  📝 Update Student                     ║")
        print("║  3.  🗑️  Delete Student                     ║")
        print("║  4.  📋 View All Students                  ║")
        print("║  5.  🔍 View Student Details               ║")
        print("║  6.  🔎 Search Student                     ║")
        print("║  7.  📚 Subject Analysis                   ║")
        print("║  8.  📊 Class Statistics                   ║")
        print("║  9.  🏆 Top Performers                     ║")
        print("║  10. ❌ Failed Students                    ║")
        print("║  11. 📤 Export Report                      ║")
        print("║  12. 🚪 Exit                               ║")
        print("╚" + "═" * 45 + "╝")

        return input("\n👉 Choice (1-12): ")

    def run(self):
        """Main application loop"""
        print("\n🎓 Welcome to Student Performance Analyzer!")

        while True:
            choice = self.show_menu()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.view_all_students()
            elif choice == '5':
                self.view_student_detail()
            elif choice == '6':
                self.search_student()
            elif choice == '7':
                self.subject_analysis()
            elif choice == '8':
                self.class_statistics()
            elif choice == '9':
                self.top_performers()
            elif choice == '10':
                self.failed_students()
            elif choice == '11':
                self.export_report()
            elif choice == '12':
                print("\n👋 Thanks for using Student Performance Analyzer!")
                print("📊 Data saved. Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

            input("\n📌 Press Enter to continue...")


# Run the application
if __name__ == "__main__":
    analyzer = StudentPerformanceAnalyzer()

    # Add sample data if empty
    if not analyzer.students:
        print("\n📝 Adding sample data...")

        sample_students = [
            ('101', 'Rahul Sharma', '10-A', {'Mathematics': 85, 'Science': 78, 'English': 92, 'Hindi': 88, 'Computer': 95}),
            ('102', 'Priya Patel', '10-A', {'Mathematics': 92, 'Science': 88, 'English': 85, 'Hindi': 90, 'Computer': 88}),
            ('103', 'Amit Kumar', '10-A', {'Mathematics': 65, 'Science': 70, 'English': 68, 'Hindi': 72, 'Computer': 75}),
            ('104', 'Sneha Singh', '10-A', {'Mathematics': 78, 'Science': 82, 'English': 80, 'Hindi': 85, 'Computer': 90}),
            ('105', 'Vikram Reddy', '10-A', {'Mathematics': 45, 'Science': 52, 'English': 48, 'Hindi': 55, 'Computer': 60}),
            ('106', 'Ananya Gupta', '10-A', {'Mathematics': 95, 'Science': 92, 'English': 90, 'Hindi': 88, 'Computer': 98}),
            ('107', 'Rohan Joshi', '10-A', {'Mathematics': 30, 'Science': 35, 'English': 42, 'Hindi': 38, 'Computer': 45}),
        ]

        for roll, name, cls, marks in sample_students:
            student = Student(roll, name, cls, marks)
            analyzer.students[roll] = student

        analyzer.save_data()
        print("✅ Sample data added!")

    analyzer.run()

