

### წარმოვიდგინოთ, რომ უნდა ამოვიცნოთ შემთხვევით რიცხვი m-დან n-მდე.
# პროგრამულად უნდა გამოვბეჭდოთ:
# m=...
# n=...
# შემთხვევითი მთელი რიცხვი შერჩეულია [m;n] შუალედიდან.
# ამოცნობილი რიცხვია: ...
# შემთხვევითი რიცხვი იყო: ...
# რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა: ...
# შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა: ...

 
# m=1                                 # m-ის ცვლილება ხდება აქ
# n=1000000000000                     # n-ის ცვლილება ხდება აქ

# if n-m<0 or m<0 or n<0:
#     print("m და n მონაცემების შეტანაში შეცდომაა დაშვებული")
# import random 
# randomN = random.randint(a=m , b=n)

# mk=m
# nk=n
# maxk=0
# if n-m <= 4 and n-m>0:
#     maxk=3

# while nk - int((mk+nk)/2) > 2:
#       maxk += 1
#       mk=int((mk+nk)/2)+1
#       if nk - int((mk+nk)/2) <= 2:
#           maxk += 2
      
# k=n-m 
# counter=0  
# number=int((n+m)/2)
# print("m=",m)
# print("n=",n) 
# print("შემთხვევითი რიცხვი შერჩეულია [m;n] შუალედიდან") 

# while True:
#     if number == randomN:
#         counter += 1
#         print("ამოცნობილი რიცხვია:", number)
#         print("შემთხვევითი რიცხვი იყო:",randomN )
#         print("რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა:", counter)
#         print("შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა:", maxk)
#         break
#     elif number < randomN and n-m>2:
#         counter += 1
#         m=number+1
#         number = int((n+m)/2)
#     elif randomN < number and n-m>2:
#         counter += 1
#         n=number-1
#         number = int((n+m)/2)
#     elif n-m == 1 and m == randomN:
#         counter += 1
#         number = m
#         print("ამოცნობილი რიცხვია:", number)
#         print("შემთხვევითი რიცხვი იყო:",randomN )
#         print("რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა:", counter)
#         print("შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა:", maxk)
#         break
#     elif n-m == 1 and n == randomN:
#         counter += 2
#         number=n
#         print("ამოცნობილი რიცხვია:", number)
#         print("შემთხვევითი რიცხვი იყო:",randomN )
#         print("რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა:", counter)
#         print("შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა:", maxk)
#         break
#     elif n-m == 2 and int((n+m)/2) == randomN:
#         counter += 2
#         number = (n+m)/2
#         print("ამოცნობილი რიცხვია:", number)
#         print("შემთხვევითი რიცხვი იყო:",randomN )
#         print("რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა:", counter)
#         print("შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა:", maxk)
#         break
#     elif n-m == 2 and int((n+m)/2) < randomN:
#         counter += 2
#         number = n
#         print("ამოცნობილი რიცხვია:", number)
#         print("შემთხვევითი რიცხვი იყო:",randomN )
#         print("რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა:", counter)
#         print("შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა:", maxk)
#         break
#     elif n-m == 2 and int((n+m)/2) > randomN:
#         counter += 2
#         number = m
#         print("ამოცნობილი რიცხვია:", number)
#         print("შემთხვევითი რიცხვი იყო:",randomN )
#         print("რიცხვის ამოსაცნობად გამოყენებული ცდების რაოდენობაა:", counter)
#         print("შერჩეული მეთოდით ცდების მაქსიმალური რაოდენობაა:", maxk)
#         break

## პროგრამა გამოიმუშავებს შემთხვევით რიცხვს m-დან n-მდე და სთხოვს მომხმარებელს გამოიცნოს რიცხვი.
# პროგრამამ უნდა გამოიყენოს while loop, რათა გააგრძელოს მომხმარებლის ჩაფიქრებული რიცხვი,
# სანამ ისინი სწორად არ გამოიცნობენ რიცხვს. მიაწოდეთ უკუკავშირი მომხმარებელს, 
# თუ მათი გამოცნობა ძალიან მაღალია ან ძალიან დაბალი.
  
# counterIs=0       #  მე შევცვალე პროგრამა შემყავს m,n საზღვრები.
# counterLover=0    # მომხმარებელს ვეხმარები სწორად გეზის არჩევაში:
# counterHigher=0   # ა) მივუთითებ მის მიერ შერჩეულ რიცხვზე დაბლებში,თუ მაღლებში ეძებოს შემთხვევითი რიცხვი.
# import random     # ბ) ვუბეჭდავ რამდენი ცდიდან, რამდენ ცდაში ამოიცნო რიცხვი.
# m=1            
# n=30              
# k=n-m         
# randomN = random.randint(a=m , b=n)
# print("m=",m)
# print("n=",n)    
# while True:
#     userN = int(input("Enter an integer from the segment [m;n]: "))
#     if userN == randomN:
#         counterIs += 1
#         counter=counterIs+counterLover+counterHigher
#         print("very good: The randomly selected number is:",userN)
#         print("The random number was recognized in",counter,"trials out of", k ,"trials")
#         break
#     elif userN > randomN:
#         counterHigher += 1
#         print("Continue searching for numbers lower than",userN)
#     elif userN < randomN:
#         counterLover += 1
#         print("Continue searching for numbers higher than",userN)













