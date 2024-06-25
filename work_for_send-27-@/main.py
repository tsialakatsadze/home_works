# შექმენით რამდენიმე json ფაილი,
# დაწერეთ მოცემული json ფაილების პარსინგი,
# დაბეჭდეთ json-ში არსებული მონაცემები


import threading
import time
from faker import Faker
import json
def generate(number):
    print("Start creating the json file")
    fake = Faker()
    data = []
    for _ in range(number):
        entity = {
                    "name": fake.name(),
                    "email": fake.email(),
                    "address": fake.address(),
                    "active": fake.boolean()
                 }
        data.append(entity)
    print("End creating the json file")
    time.sleep(1)
    print("Start splitting by property")
    active_stud = []
    inactive_stud = []
    for entity in data:
        if entity["active"]:
            active_stud.append(entity)
        else:
            inactive_stud.append(entity)
    all_stud = {"active_students": active_stud, "inactive_students": inactive_stud}
    with open("all_students.json", "w") as file:
        json.dump(all_stud, file, indent=2)
    print("End splitting by property")
    time.sleep(1)
    print("Start printing active_students")
    active_stud={"active_students": active_stud}
    print(active_stud)
    print("End printing active_students")
    time.sleep(1)
    print("Start printing inactive_students")
    inactive_stud = {"inactive_students": inactive_stud}
    print(inactive_stud)
    print("End printing inactive_students")
    time.sleep(1)

number = 20
generate(number)

print(threading.active_count())
print(threading.enumerate())

