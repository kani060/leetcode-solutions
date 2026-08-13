# 2. Student Result System — Encapsulation Concept: Encapsulation and Class Design Create a Student class containing name, roll number and marks for five subjects.
# Requirements: • Marks must be between 0 and 100. • Calculate total, average and grade. • 
# Marks must not be directly modified from outside the class. • Create at least three students and display their results.

class Student:

    def __init__(self, name, rollNumber, marks):
        self.name = name
        self.rollNumber = rollNumber
        self.__marks = marks

    def setMarks(self, marks):
        if len(marks) != 5:
            print("Marks must be given for 5 subjects")
            return
        for mark in marks:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100")
                return

        self.__marks = marks

    def getMarks(self):
        return self.__marks

    def calculateTotal(self):
        total = 0
        for mark in self.__marks:
            total += mark
        return total

    def calculateAverage(self):
        return self.calculateTotal() / 5

    def calculateGrade(self):
        average = self.calculateAverage()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def displayResult(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollNumber)
        print("Marks:", self.getMarks())
        print("Total:", self.calculateTotal())
        print("Average:", self.calculateAverage())
        print("Grade:", self.calculateGrade())
student1 = Student("Kanisgha", 101, [90, 85, 95, 88, 92])
student2 = Student("Sujay", 102, [75, 80, 72, 78, 85])
student3 = Student("Priya", 103, [60, 65, 58, 70, 62])
student1.displayResult()
student2.displayResult()
student3.displayResult()
