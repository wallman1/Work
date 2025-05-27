from Schoolsystem import *

student1 = Student("Jimbo","Jones","25/12/2012", "Male", "Jimbo.Jones@edu.state.gov.country",7,123456789,"Red house")
parent1 = Parent("John","Doe","11/11/1990","Male", "John.Doe@Corporation.org","Jimbo Jones",5550100)
teacher1 = Teacher("Mrs","Smith","12/12/1999","Female","Mrs.Smith@det.gov.state.country",987654321, "Math")

teacher1.get_details()
teacher1.get_age()
teacher1.get_faculty()
teacher1.get_id()

parent1.get_num()
parent1.get_child()

student1.get_id()
student1.get_details()