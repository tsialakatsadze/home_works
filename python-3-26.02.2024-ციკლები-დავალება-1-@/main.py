 
# 1. დაწერეთ პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. 
# შექმენით საწყისი ცვლადი total_sum =0, შეამოწმეთ რიცხვი თუ დადებითია,
# მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. 
# ეს პროცესი გაგრძელდეს იქამდე სანამმომხმარებელი არ შეიყვანს 'sum' ტექსტს, 
# რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

# total_sum = 0
# while True:
#   a = input("Enter the data: ")
#   if str(a) == 'sum':
#     False
#     print("total= ", total_sum)
#     break
#   elif float(a)>0:
#     total_sum += float(a)
#   elif float(a)<=0:
#     total_sum += 0

# 2. გამოთვალეთ რიცხვების ჯამი, სანამ მომხმარებელი არ შეიყვანს 0-ს

# total = 0
# while True:
#   a = input("Enter a number: ")
#   if float(a) == 0:
#     False
#     print("total= ", total)
#     break
#   elif float(a)>0 or float(a)<0:
#     total += float(a)
  
# 3. რომელიც გამოიმუშავებს შემთხვევით რიცხვს m-დან n-მდე და სთხოვს მომხმარებელს გამოიცნოს რიცხვი.
# პროგრამამ უნდა გამოიყენოს while loop, რათა გააგრძელოს მომხმარებლის ჩაფიქრებული რიცხვი,
# სანამ ისინი სწორად არ გამოიცნობენ რიცხვს. მიაწოდეთ უკუკავშირი მომხმარებელს, 
# თუ მათი გამოცნობა ძალიან მაღალია ან ძალიან დაბალი.
  
counterIs=0       #  მე შევცვალე პროგრამა შემყავს m,n საზღვრები.
counterLover=0    # მომხმარებელს ვეხმარები სწორად გეზის არჩევაში:
counterHigher=0   # ა) მივუთითებ მის მიერ შერჩეულ რიცხვზე დაბლებში,თუ მაღლებში ეძებოს შემთხვევითი რიცხვი.
import random     # ბ) ვუბეჭდავ რამდენი ცდიდან, რამდენ ცდაში ამოიცნო რიცხვი.
m=1           # გ) ვუბეჭდავ შერჩეული მეთოდით დაახლოებით რისი ტოლი იქნება "რიცხვის ამოცნობის ალბათობა".  
n=30              
k=n-m         
randomN = random.randint(a=m , b=n)
print("m=",m)
print("n=",n)    
while True:
    userN = int(input("Enter an integer from the segment [m;n]: "))
    if userN == randomN:
        False
        counterIs += 1
        counter=counterIs+counterLover+counterHigher
        print("very good: The randomly selected number is:",userN)
        print("The random number was recognized in",counter,"trials out of", k ,"trials")
        print("The probability that you will recognize the number is: ", 1-float(counter/k))
        # რაც უფრო ნაკლებია ცდების რაოდენობა, მით უფრო მეტია ამოცნობის ალბათობა.
        break
    elif userN > randomN:
        counterHigher += 1
        print("Continue searching for numbers lower than",userN)
    elif userN < randomN:
        counterLover += 1
        print("Continue searching for numbers higher than",userN)
    
  
 
  


