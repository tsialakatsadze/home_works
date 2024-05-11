
# შექმენით კლასი Student რომელიც მიიღებს სამ მნიშვნელობას სახელს ასაკს და ლისტში ჩაწერილ ქულებს.
# კლასს ექნება სამი მეთოდი, პირველი მეთოდი იქნება ჯსონის წაკითხვა,
# მეორე მეთოდი იქნება ქულის საშუალო არითმეტიკულის დაანაგრიშება 
# და მესამე იქნება ჯსონ ფაილში ამ ინფორმაციის ჩაწერა.


import json

class Student:
     def __init__(self, name, age, grades):
         self.name = name
         self.age = age
         self.grades = grades
     def to_json(self):
         average = sum(self.grades)/len(self.grades)
         return {'name': self.name, 'age': self.age,'grades': self.grades, 'average': average }
     def from_json(self):
          self.average = average
          name = self[name]
          age = self[age]
          grades = self[grades]
          average = self[average]
          return Student(name,age,grades,average)
    
student_1 = Student('Alice', 20 , [85, 90, 75])
to_json_stud_1 = json.dumps(student_1.to_json(),indent=3)
print(to_json_stud_1)
student_2 = Student('Bob', 21 , [80, 88, 92])
to_json_stud_2 = json.dumps(student_2.to_json(),indent=3)
print(to_json_stud_2)
student_3 = Student('Charlie', 22 ,[70, 75, 65])
to_json_stud_3 = json.dumps(student_3.to_json(),indent=3)
print(to_json_stud_3)

