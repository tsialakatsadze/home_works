#  ამოცანა : უნდა დავწერო პითონის ფუნქცია,
#  რომელიც დამიანგარიშებს რეკურსიის მე-n-ე წევრს, როდესაც მიმდევრობის პირველი და მეორე წევრებია a_1, a_2,
#  ხოლო რეკურსიით, ყოველი მომდევნო წევრი დაწყებული მესამედან წინა ორი წევრის ჯამია.
# მაგ.: ფიბონაჩის მიმდევრობაა 1,1,2,3,5,8,13,21,34,55,89,144,233... 


def recursion(a_1,a_2,n):  # n>=3 and a_n = a_n-2 + a_n-1
 a=[a_1,a_2]
 i=1
 while i <=n-2:
    i += 1
    a.append(a[i-2]+a[i-1])
    if i==n-1:
       return a[n-1]
w=1
v=1
h=13
print(recursion(w,v,h))   # 233

w=1
v=1
h=30
print(recursion(w,v,h))   # 832040


# მოცემული დავალება:
# შექმენით ფუნქცია სახელად print_pattern,
# რომელიც იღებს რიცხვს პარამეტრად და ბეჭდავს შაბლონს ამ რიცხვზე დაყრდნობით.
# მაგალითად, თუ შევიყვანთ  5, ფუნქციამ უნდა დაბეჭდოს ასეთი ნიმუში:
1
12
123
1234
12345

def print_pattern(n):
  b="1"
  print(b)
  i=1
  while i < n :
   i += 1
   b=b + str(i)
   print(b)
  
print_pattern(20)

