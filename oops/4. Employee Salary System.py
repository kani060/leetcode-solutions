# 4. Employee Salary System — Inheritance and Polymorphism Concept: Inheritance and Runtime Polymorphism Create Employee with child classes Developer, Designer and Manager.
# Every employee must have calculateSalary(), but the salary calculation must be different for each employee. For example: • Developer — basic salary + coding bonus 
# • Designer — basic salary + design bonus • Manager — basic salary + management bonus Store all employees in a common collection and calculate their salaries using the same method call.

class Employee:

    def __init__(self, name, basicSalary):
        self.name = name
        self.basicSalary = basicSalary

    def calculateSalary(self):
        return self.basicSalary


class Developer(Employee):

    def __init__(self, name, basicSalary, codingBonus):
        super().__init__(name, basicSalary)
        self.codingBonus = codingBonus

    def calculateSalary(self):
        return self.basicSalary + self.codingBonus


class Designer(Employee):

    def __init__(self, name, basicSalary, designBonus):
        super().__init__(name, basicSalary)
        self.designBonus = designBonus

    def calculateSalary(self):
        return self.basicSalary + self.designBonus


class Manager(Employee):

    def __init__(self, name, basicSalary, managementBonus):
        super().__init__(name, basicSalary)
        self.managementBonus = managementBonus

    def calculateSalary(self):
        return self.basicSalary + self.managementBonus
developer = Developer("Arun", 50000, 10000)
designer = Designer("Priya", 45000, 8000)
manager = Manager("Rahul", 60000, 15000)
employees = [developer, designer, manager]
for employee in employees:
    print(employee.name, "Salary:", employee.calculateSalary())
