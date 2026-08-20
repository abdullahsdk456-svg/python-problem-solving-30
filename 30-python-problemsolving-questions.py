# 30 Python Problem Solving Questions
# Questions with simple answers and outputs

# =========================
# Q1. Change PIN
# =========================

# Question:
# Fix the error in the change_pin function.

def change_pin(self, old_pin, new_pin):
    if self.pin == old_pin:
        self.pin = new_pin
        print("Pin changed successfully")
    else:
        print("Incorrect old pin")

# Answer:
# The problem was that old_pin should be used for checking the old PIN.


# =========================
# Q2. ATM Login and Transactions
# =========================

# Question:
# What will be the output?

# atm = ATM(1234, 10000)
# atm.login(1234)
# atm.check_balance()
# atm.deposit(50000)
# atm.withdraw(2000)
# atm.change_pin(1234, 3421)

# Answer:
# Login successful
# Current Balance 10000
# Deposit Successfully
# Current Balance 60000
# Withdrawal Successfully
# Current Balance 58000
# Pin changed successfully


# =========================
# Q3. Deposit Validation
# =========================

# Question:
# Add a condition so that the user cannot deposit a negative amount.

def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print("Deposit Successfully")
    else:
        print("Invalid amount")


# Output:
# Deposit Successfully
# or
# Invalid amount


# =========================
# Q4. Withdraw Validation
# =========================

# Question:
# Add a condition for insufficient balance.

def withdraw(self, amount):
    if amount > self.balance:
        print("Insufficient balance")
    else:
        self.balance -= amount
        print("Withdrawal Successfully")


# Output:
# Withdrawal Successfully
# or
# Insufficient balance


# =========================
# Q5. Withdraw More Than Balance
# =========================

# Question:
# What happens when the user withdraws more money than the balance?

# atm = ATM(1234, 10000)
# atm.withdraw(15000)

# Answer:
# Insufficient balance


# =========================
# Q6. __init__ Method
# =========================

# Question:
# What is the purpose of __init__?

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

# Answer:
# __init__ is used to give initial values to an object.


# =========================
# Q7. Wrong PIN
# =========================

# Question:
# What happens if the user enters the wrong PIN?

# atm = ATM(1234, 10000)
# atm.login(1111)

# Answer:
# Incorrect pin


# =========================
# Q8. Object Creation
# =========================

# Question:
# Create an ATM object and call the login method.

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def login(self, pin):
        if self.pin == pin:
            print("Login successful")
        else:
            print("Incorrect pin")


atm = ATM(1234, 10000)
atm.login(1234)

# Output:
# Login successful


# =========================
# Q9. Abstract Method
# =========================

# Question:
# What is the use of @abstractmethod?

from abc import ABC, abstractmethod

class BankTemplate(ABC):

    @abstractmethod
    def show_balance(self):
        pass

# Answer:
# It makes a method compulsory for the child class.


# =========================
# Q10. Encapsulation
# =========================

# Question:
# Use a private variable for balance.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

# Answer:
# __balance is a private variable.
# It is used for encapsulation.


# =========================
# Q11. Get Balance
# =========================

# Question:
# Create a method to get the private balance.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount("Ali", 1000)
print(account.get_balance())

# Output:
# 1000


# =========================
# Q12. Withdraw From Account
# =========================

# Question:
# What happens if we withdraw more than the balance?

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal Successfully")


account = BankAccount(1000)
account.withdraw(1500)

# Output:
# Insufficient balance


# =========================
# Q13. Deposit and Withdraw
# =========================

# Question:
# Deposit 100, deposit 200 and withdraw 300.

balance = 1000

balance = balance + 100
print(balance)

balance = balance + 200
print(balance)

balance = balance - 300
print(balance)

# Output:
# 1100
# 1300
# 1000


# =========================
# Q14. Set Balance
# =========================

# Question:
# Do not allow a negative balance.

def set_balance(self, balance):
    if balance >= 0:
        self.__balance = balance
    else:
        print("Balance cannot be negative")


# Output:
# Balance cannot be negative


# =========================
# Q15. Abstract Transaction
# =========================

# Question:
# Create an abstract transaction method.

class BankTemplate(ABC):

    @abstractmethod
    def transaction(self, services, amount):
        pass

# Answer:
# The child class has to define this method.


# =========================
# Q16. Inheritance
# =========================

# Question:
# Make bank_account inherit from BankTemplate.

class bank_account(BankTemplate):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# Answer:
# bank_account is now a child class of BankTemplate.


# =========================
# Q17. List Slicing
# =========================

# Question:
# Find the output.

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

print(my_list[2:5])
print(my_list[4:])
print(my_list[:6])

# Output:
# ['o', 'g', 'r']
# ['r', 'a', 'm']
# ['p', 'r', 'o', 'g', 'r', 'a']


# =========================
# Q18. append and extend
# =========================

# Question:
# Add items to a list using append and extend.

fruits = ['apple', 'banana', 'lychee']

fruits.append('cherry')
fruits.extend(['mango', 'grape'])

print(fruits)

# Output:
# ['apple', 'banana', 'lychee', 'cherry', 'mango', 'grape']


# =========================
# Q19. List and Tuple
# =========================

# Question:
# Show the difference between a list and a tuple.

fruits = ['apple', 'banana', 'lychee']
fruits_tuple = ('apple', 'banana', 'lychee')

print(fruits)
print(fruits_tuple)

# Output:
# ['apple', 'banana', 'lychee']
# ('apple', 'banana', 'lychee')

# Answer:
# List can be changed but tuple cannot be changed.


# =========================
# Q20. Tuple Check
# =========================

# Question:
# Find the output.

fruits = ('apple', 'banana', 'lychee')

for fruit in fruits:
    print(fruit)

print('cherry' in fruit)

# Output:
# apple
# banana
# lychee
# False


# =========================
# Q21. del Keyword
# =========================

# Question:
# Delete a list using del.

fruits = ['apple', 'banana', 'lychee']

print(fruits)
del fruits

# Output:
# ['apple', 'banana', 'lychee']


# =========================
# Q22. Add Items in List
# =========================

# Question:
# Add cherry and mango to the list.

fruits = ['apple', 'banana', 'lychee']

fruits.append('cherry')
fruits.append('mango')

print(fruits)

# Output:
# ['apple', 'banana', 'lychee', 'cherry', 'mango']


# =========================
# Q23. Tuple Unpacking
# =========================

# Question:
# Unpack the tuple into three variables.

number = (1, 2, -4)

a, b, c = number

print(a)
print(b)
print(c)

# Output:
# 1
# 2
# -4


# =========================
# Q24. Set Duplicates
# =========================

# Question:
# Remove duplicate values from a set.

my_set = {2, 32, 3, 3, 4, 2, 4}

print(my_set)

# Output:
# {2, 3, 4, 32}

# Answer:
# Set does not store duplicate values.


# =========================
# Q25. Empty Set
# =========================

# Question:
# Create an empty set.

empty_set = set()

print(empty_set)

# Output:
# set()


# =========================
# Q26. add and update
# =========================

# Question:
# Add one item and multiple items to a set.

student = {'ali', 3232, 'ahmad'}

student.add('zafar')
student.update(['ammar', 'usman'])

print(student)

# Output:
# The order can be different because sets are unordered.


# =========================
# Q27. Set With Different Values
# =========================

# Question:
# Is this a valid set?

studentid = {111, 112.332, 121}

print(studentid)

# Answer:
# Yes, this is a valid set.


# =========================
# Q28. if Condition
# =========================

# Question:
# Check if any subject marks are greater than 100.

sub1 = 110
sub2 = 80
sub3 = 70

if sub1 > 100 or sub2 > 100 or sub3 > 100:
    print("Error: marks cannot be greater than 100")

# Output:
# Error: marks cannot be greater than 100


# =========================
# Q29. Student Input
# =========================

# Question:
# Take input for 5 students.

for i in range(5):
    name = input("Enter your name: ")
    sub1 = int(input("Enter first subject marks: "))
    sub2 = int(input("Enter second subject marks: "))
    sub3 = int(input("Enter third subject marks: "))

# Output:
# Enter your name:
# Enter first subject marks:
# Enter second subject marks:
# Enter third subject marks:


# =========================
# Q30. range Function
# =========================

# Question:
# Print numbers from 1 to 50.

for i in range(1, 51):
    print(i)

# Output:
# 1
# 2
# 3
# ...
# 50
