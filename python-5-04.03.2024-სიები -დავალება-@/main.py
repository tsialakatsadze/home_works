
# 2) დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]], 
# და შეასრულებს შემდეგ ნაბიჯებს: 
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა 
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello" 
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს 
# d. შექმენით ახალი ლისტი my_llist_2

# my_llist = [43, '22', 12, 66, 210, ["hi"]]
# print(my_llist.index(210))     #  4
# print(my_llist.index('22'))    #  1
# print(my_llist.index(["hi"]))  #  5

# my_llist.append("hello")
# print(my_llist)                #  [43, '22', 12, 66, 210, ["hi"], 'hello']

# my_llist.remove(my_llist[2])
# print(my_llist)
# my_llist_2=my_llist
# print(my_llist_2)


# 3) დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული nxn მატრიცის ტრანსპონირებას, 
# ტრანსპონირება ნიშნავს ინდექსების შებრუნებას, 
# მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3],
# ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე

n=5
matrix=[
       [0.0, 0.1, 0.2, 0.3, 0.4],
       [1.0, 1.1, 1.2, 1.3, 1.4],
       [2.0, 2.1, 2.2, 2.3, 2.4],
       [3.0, 3.1, 3.2, 3.3, 3.4],
       [4.0, 4.1, 4.2, 4.3, 4.4]
       ]
print("მოცემული იყო მატრიცა:",n,"x",n)
for i in range(n):
    print(matrix[i])
matrix_transp=matrix
i=0
j=i+1
while j <= n-1:
    m = matrix_transp[i][j]
    matrix_transp[i][j] = matrix_transp[j][i]
    matrix_transp[j][i] = m
    j += 1
    if j == n and i < n-2:
       i += 1
       j=i+1
if j == n and i == n-2:
 print("მოცემული მატრიცის  ტრანსპონირებული მატრიცა იქნება:")
 for k in range(n):
    print(matrix_transp[k])



# n=4
# matrix=[
#        [0.0, 0.1, 0.2, 0.3],
#        [1.0, 1.1, 1.2, 1.3],
#        [2.0, 2.1, 2.2, 2.3],
#        [3.0, 3.1, 3.2, 3.3]
#        ]
# print("მოცემული იყო მატრიცა:",n,"x",n)
# for i in range(n):
#     print(matrix[i])
# matrix_transp=matrix
# i=0
# j=i+1
# while j <= n-1:
#     m = matrix_transp[i][j]
#     matrix_transp[i][j] = matrix_transp[j][i]
#     matrix_transp[j][i] = m
#     j += 1
#     if j == n and i < n-2:
#        i += 1
#        j=i+1
# if j == n and i == n-2:
#  print("მოცემული მატრიცის  ტრანსპონირებული მატრიცა იქნება:")
#  for k in range(n):
#     print(matrix_transp[k])



# n=3
# matrix=[
#        [0.0, 0.1, 0.2],
#        [1.0, 1.1, 1.2],
#        [2.0, 2.1, 2.2]
#        ]
# print("მოცემული იყო მატრიცა:",n,"x",n)
# for i in range(n):
#     print(matrix[i])
# matrix_transp=matrix
# i=0
# j=i+1
# while j <= n-1:
#     m = matrix_transp[i][j]
#     matrix_transp[i][j] = matrix_transp[j][i]
#     matrix_transp[j][i] = m
#     j += 1
#     if j == n and i < n-2:
#        i += 1
#        j=i+1
# if j == n and i == n-2:
#  print("მოცემული მატრიცის  ტრანსპონირებული მატრიცა იქნება:")
#  for k in range(n):
#     print(matrix_transp[k])



# n=2
# matrix=[
#        [0.0, 0.1],
#        [1.0, 1.1]
#        ]
# print("მოცემული იყო მატრიცა:",n,"x",n)
# for i in range(n):
#     print(matrix[i])
# matrix_transp=matrix
# i=0
# j=i+1
# while j <= n-1:
#     m = matrix_transp[i][j]
#     matrix_transp[i][j] = matrix_transp[j][i]
#     matrix_transp[j][i] = m
#     j += 1
#     if j == n and i < n-2:
#        i += 1
#        j=i+1
# if j == n and i == n-2:
#  print("მოცემული მატრიცის  ტრანსპონირებული მატრიცა იქნება:")
#  for k in range(n):
#     print(matrix_transp[k])
 




