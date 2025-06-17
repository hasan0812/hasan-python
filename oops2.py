# class Animal():
#     def __init__(self, name)
#     print(f"{self.name}'s object has been created")

#     def sound(self):
#         print(f"{self.name} is now making sound")

#      def walk(self):
#          print(f"{self.name} object is now walking")

#      def __init__(self):
#         print(f"{self.name} object has been deleted")

# dog = Animal("buddy")
# dog.sound()
# dog.walk

# cat = Animal("billu")
# cat.sound()
# cat.walk()

# del dog
# del cat
# cat.sound()

class Student:
    def __init__(self, name, age, grade)

    self.name = name
    self.age = age
    self.grade = grade
    print(f"/nStudent record created for {self.name}.")

    def showDetails(self):
        print(f"Name: {self.name}")
         print(f"Age: {self.age}")
         print(f"Grade: {self.grade}")

     def updateGrade(self, new_grade)
     print(f"Student record for {self.name has been deleted}")


if __name__ == "__main__":
    print("Welcome to the Student Manegement System")


    student1 = Student("Anjali", 14 "8")
    student1.showDetails()

    print("/nUpdating student grade...")
    student1.updateGrade("9th")
    del student1


