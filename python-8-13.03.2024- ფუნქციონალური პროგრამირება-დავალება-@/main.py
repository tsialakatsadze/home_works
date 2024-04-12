
# 1.დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს მთელი რიცხვი
# და აგდებს ValueError შეცდომას, თუ შეყვანილი მონაცემი არ არის სწორი.(მთელი რიცხვი მაგალითად)

# while True:
#     try:      
#       user=int(input("შემოიყვანეთ მთელი რიცხვი: "))
#     except ValueError:
#       print("    შემოტანილი რიცხვი მთელი არ არის ")

  
      
# 2. დაწერეთ ფუნქცია სახელად divide,რომელიც იღებს ორ პარამეტრს, მრიცხველს და მნიშვნელს 
#  და აბრუნებს გაყოფის შედეგს.    
      
# def divide(divide,separator):
#     try:
#       division = float(divide)/float(separator)
#       return division
#     except ZeroDivisionError:
#       print("ნულზე გაყოფა არ შეიძლება")
#     except Exception as error:
#       print("error")
# while True:
#    m=input("შემოიყვანეთ გასაყოფი: ") 
#    n=input("შემოიყვანეთ გამყოფი: ")
#    print(divide(m,n))

# 3. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს(ending).
# დააბრუნეთ მხოლოდ ის სიის ელემენტები, რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (exeptions)
# მაგალითად
# Lst = ['hello', 'world', 'coding', 'nod']
# End = ing
# დაგვიბრუნებს [‘coding’]

def selection(words,end):
    try:
     k=len(end)
     new_list = list(filter(lambda x: x[len(x)-k:len(x)] == end, words))
     return(new_list)
    except Exception as error:
     print("There are errors in data selection")


# მაგალითები:

list_1=[2125,425,25,75,525,7125,125,85,11,17,65]
end='5'
print("-1- Given are symbols ",list_1)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_1,end))
print(' ')

list_1=['2125','425','25','75','525','7125', '125', '85','11', '17','65']
end='5'
print("-2- Given are symbols ",list_1)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_1,end))
print(' ')


list_1=['2125','425','25','75','525','7125', '125', '85','11', '17','65']
end='25'
print("-3- Given are symbols ",list_1)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_1,end))
print(' ')

list_1=['2125','425','25','75','525','7125', '125', '85','11', '17','65']
end='125'
print("-4- Given are symbols ",list_1)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_1,end))
print(' ')

list_1=['hello','coding','world','map','filter','pading', 'teaching', 'training', 'studying']
end='ing'
print("-5- Given are symbols ",list_1)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_1,end))
print(' ')

list_2=['hello','world','map']
end='ing'
print("-6- Given are symbols ",list_2)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_2,end))
print(' ')

list_3=123
end=3
print("-7- Given are symbols ",list_3)
print("The ending of the selected symbols is:",end)
print("return")
print(selection(list_3,end))
print(' ')
