import datetime

class Person:
    def __init__(self, fname ,surname,dob, gender, email):
        self.fname = fname
        self.surname = surname
        self.dob = dob
        self.gender = gender
        self.email = email

    def get_age(self):
        print(f"{self.fname} {self.surname}'s date of birth is {self.dob}")

    def get_details(self):
        print(f"First Name: {self.fname}, Surname: {self.surname}, Dob: {self.dob}, Gender: {self.gender}, Email: {self.email}")

class Student(Person):
    def __init__(self, fname, surname, dob, gender, email, Year, studentid, house):
        super().__init__(fname, surname, dob, gender, email)
        self.Year = Year
        self.studentid = studentid
        self.house = house

    def get_id(self):
        print(f"{self.fname} {self.surname} with ID: {self.studentid} is a student at this school.")

class Teacher(Person):
    def __init__(self, fname, surname, dob, gender, email, staff_id, faculty):
        super().__init__(fname, surname, dob, gender, email)
        self.staff_id = staff_id
        self.faculty = faculty

    def get_faculty(self):
        print(f"{self.fname} is part of the {self.faculty} faculty.")

    def get_id(self):
        print(f"{self.fname} {self.surname} with ID: {self.staff_id} is a teacher at this school.")

class Parent(Person):
    def __init__(self, fname, surname, dob, gender, email, child, pnumber):
        super().__init__(fname, surname, dob, gender, email)
        self.child = child
        self.pnumber = pnumber

    def get_num(self):
        print(f"{self.fname}'s phone number is {self.pnumber}")

    def get_child(self):
        print(f"{self.fname}'s child is {self.child}")