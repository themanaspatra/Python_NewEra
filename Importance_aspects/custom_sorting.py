# ------------------------------------------------------------------------
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

e1 = Employee("steve", 26, 1000)
e2 = Employee("jobs", 30, 800)
e3 = Employee("bill", 31, 1200)
e4 = Employee("gates", 17, 1400)

employees = [e1, e2, e3, e4]

# sorting the list of employees based on "age"
by_age = sorted(employees, key=lambda employee: employee.age)
by_name = sorted(employees, key=lambda employee: employee.name)
by_pay = sorted(employees, key=lambda employee: employee.pay)
# ------------------------------------------------------------------------

class BankAccount:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

c1 = BankAccount("steve", 17, 1000)
c2 = BankAccount("jobs", 26, 800)
c3 = BankAccount("tammy",18, 2000)
c4 = BankAccount("bill", 26, 1200)

customers = [c1, c2, c3, c4]

by_name = sorted(customers, key=lambda customer: customer.name)
by_age = sorted(customers, key=lambda customer: customer.age)
by_balance = sorted(customers, key=lambda customer: customer.balance)

# modifies the original list
customers.sort(key=lambda customer: customer.name)
customers.sort(key=lambda customer: customer.age)
customers.sort(key=lambda customer: customer.balance)

# ------------------------------------------------------------------------
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


s1 = Student("dave", 'A', 26)
s2 = Student('john', 'C', 28)
s3 = Student('jane', 'B', 24)

students = [s1, s2, s3]

by_name = sorted(students, key=lambda student: student.name)
by_grade = sorted(students, key=lambda student: student.grade)
by_age = sorted(students, key=lambda student: student.age)

# this modifies the original list
students.sort(key=lambda student: student.name)
students.sort(key=lambda student: student.age)
students.sort(key=lambda student: student.grade)

# ------------------------------------------------------------------------

