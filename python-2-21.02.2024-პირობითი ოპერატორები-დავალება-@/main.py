

# 1. დაწერეთ პროგრამა, რომელიც მიიღებს მოსწავლის ქულებს, 
# როგორც შეყვანის სახით და დაბეჭდავს მათ შესაბამის შეფასებას (A, B, C და ა.შ.) 
# if-elif-else ოპერატორების გამოყენებით.
#  A = 91-100   B = 81-90   C = 71 - 80   D = 61 - 70   E = 51 - 60   F=0-50

# score=int(input("enter score: "))
# if score>=91 and score<=100:
#     result='A'
# elif score>=81 and score<=90:
#     result='B'
# elif score>=71 and score<=80:
#     result='C'
# elif score>=61 and score<=70:
#     result='D'
# elif score>=51 and score<=60:
#     result='E'
# elif score>=0 and score<=50:
#     result='F'
# else:
#     print('The data is incorrect')

# print("Result: ", result)    


# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას.
# თუ რიცხვი ლუწია გამოიტანეთ ტექსტი ‘even’ თუ კენტია ‘odd’

# number=int(input("enter namber: "))
# if number % 2 == 0:
#     print(number,"is an even number")
# else:
#     print(number,"is an odd number")


# 3. დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში 
# მოძებნის სიტყვებს “small”, “tall”, “middle”
# a. თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაბეჭდეთ პირველივე სიტყვა რაც აღმოჩნდება ტექსტში
# b. თუ ტექსტში არცერთი სიტყვა მოიძებნა დაბეჭდეთ, რომ ტექსტში ეს სამი სიტყვა არ მოიძებნა

# პროგრამის შესამოწმებლად დააკოპირეთ და ჩასვით
# Shop Wayfair for all the best small tall middle Kitchen. 
# Shop Wayfair for all the best tall middle Kitchen. 
# Shop Wayfair for all the best tall small Kitchen.
# Shop Wayfair for all the best middle small Kitchen.
# Shop Wayfair for all the best middle Kitchen. 
# Shop Wayfair for all the best tall Kitchen.
# Shop Wayfair for all the best small Kitchen.
# Two colors in black is for your.


list_1=str(input("enter text: "))
counter=0
small="small" in list_1
tall="tall" in list_1
middle="middle" in list_1
if small == True:
    counter += 1
    print("The word small was found in the text")
elif tall == True:
   counter += 1
   print("The word tall was found in the text")
elif middle == True:
   counter += 1
   print("The word middle was found in the text")
elif counter == 0:
  print("The words small, tall, middle could not be found in the text")

       



