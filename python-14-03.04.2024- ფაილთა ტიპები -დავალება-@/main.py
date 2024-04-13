
# me-14 leqciis davaleba
# შექმენით ხელით რაიმე csv ფაილი და 
# შემდგომ წაიკითხეთ ამ ფაილიდან სახელი და გვარი, 
# რა საგანს სწავლობს და ამ საგნის ქულა მაგალითი:
# FullName,Subject,Score
# giorgi gelashvili,matematika,90
# giorgi gelashvili,kimia,10
# gela gociridze,matematika,20
# gela gociridze,kimia,20

# ამის შემდგომ წაიკითხეთ მოცემული ქულები 
# და გაიგეთ საშუალო არითმეტიკული ამ პიროვნების რომელსაც შემდგომ დაპრინტავთ:
# 
# სტუდენტის ქულა {'giorgi gelashvili': [90, 10], 'gela gociridze': [20, 20]}
# საშუალო ქულა:  {'giorgi gelashvili': 50.0, 'gela gociridze': 20.0}

import csv

my_class=[
    {"fulname": "giorgi gelashvili", "subject": "matematika", "score": 90 },
    {"fulname": "giorgi gelashvili", "subject": "qimia", "score": 70},
    {"fulname": "gela gociridze", "subject": "matematika", "score": 80},
    {"fulname": "gela gociridze", "subject": "qimia", "score": 60 },
    {"fulname": "nodar lomidze", "subject": "matematika", "score": 100},
    {"fulname": "nodar lomidze", "subject": "qimia", "score": 50},
    {"fulname": "mariam popxadze", "subject": "matematika", "score": 40 },
    {"fulname": "mariam popxadze", "subject": "qimia", "score": 30},
    {"fulname": "nini kupatadze", "subject": "matematika", "score": 70},
    {"fulname": "nini kupatadze", "subject": "qimia", "score": 40},
    {"fulname": "nana komladze", "subject": "matematika", "score": 70},
    {"fulname": "nana komladze", "subject": "qimia", "score": 100},
]

header=["fulname", "subject", "score"]

with open("class.csv", "w") as new_csv:
    writer = csv.DictWriter(new_csv, fieldnames = header,delimiter=";")
    writer.writeheader()
    writer.writerows(my_class)

with open("class.csv", "r") as read_csv:
    csv_reader = csv.DictReader(read_csv, delimiter=";")
    csv_rows=list(csv_reader)


the_keys_is = [
     "giorgi gelashvili", 
     "gela gociridze", 
     "nodar lomidze",
     "mariam popxadze",
     "nini kupatadze",
     "nana komladze"
]
scores_dict={}
average_dict={}
the_scores_is=[]
average_scores_is=[]
i=0
while i < len(the_keys_is):
    scores=[csv_rows[2*i]["score"],csv_rows[2*i+1]["score"]]
    average = (int(csv_rows[2*i]["score"]) + int(csv_rows[2*i+1]["score"]))/2
    the_scores_is.append(scores)
    average_scores_is.append(average)
    i += 1
    if i == len(the_keys_is):
       break
for i in range(len(the_keys_is)):
    scores_dict[the_keys_is[i]] = the_scores_is[i]
print(scores_dict)

for i in range(len(the_keys_is)):
    average_dict[the_keys_is[i]] = average_scores_is[i]
print(average_dict)
