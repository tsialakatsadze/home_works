
# 1. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს არგუმენტს,
# პირობითად num_1 და num_2-ს შემდეგ ამის და მიხედვით შექმნის ლისტს 
# და საბოლოოდ დაგვიბრუნებს ლისტში არსებული ყველა ობიექტის კვადრატს



# def func_1(num_1,num_2):
#     b=[num_1**2, num_2**2]
#     return(b)
    

# m = 13
# n = 12
# print(func_1(m,n)) # [169,144]

# k=m**2 - n**2   
# t=m**2 + n**2
# print(func_1(k,t))   #[625, 97969]


#2 ჩემი გამოგონებული: უნდა დავწერო პითონის ფუნქცია, რომელიც დამიანგარიშებს რეკურსიის მე-n-ე წევრს.
#  ვიცით მიმდევრობის პირველი და მეორე წევრები num_1,num_2.
#  რეკურსია ასეთია: ყოველი მომდევნო წევრი დაწყებული მესამედან წინა ორი წევრის ჯამია.
# მაგ.: ფიბონაჩის მიმდევრობაა 1,1,2,3,5,8,13,21,34,55,89,144,233... 

def func_2(num_1,num_2,n):
    i=1
    a=num_1
    b=num_2
    while i <= n-2:
       i += 1
       c=b
       b=a+b
       a=c
       if i == n-1:
           return(b)

w=1
v=1
h=13
print(func_2(w,v,h)) # 233

w=1
v=1
h=30
print(func_2(w,v,h)) 


