
# Faker-ის გამოყენებით დააგენერირეთ 100 ჩანაწერი სტუდენტების შესახებ ჯსონში 
# და შემდგომ დაახარისხეთ ის აქტიურ და არა აქტიურ სტუდენტებად, შეასრულეთ ეს დავალება კლასების გამოყენებით.

from faker import Faker
import json

class Students:
    
    def __init__(self,number):
        self.number = number
    def generate(number):
        fake = Faker()
        data=[]
        for _ in range(number):
            entity = {
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
            "active": fake.boolean()
        }
            
            data.append(entity)
        return  data       
        

r_data = Students
fake_students = r_data.generate(100)
active_stud = []
inactive_stud = []
for entity in fake_students:
    if entity["active"]:
        active_stud.append(entity)
    else:
        inactive_stud.append(entity)
    all_stud = {"active_students": active_stud, "inactive_students": inactive_stud }    
    with open("all_students.json", "w") as file:
        json.dump(all_stud, file, indent=2)




