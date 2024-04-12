# 1.იპოვნეთ ლისტში გამოტოვებული რიცხვი 

def finding_the_missing_numbers(m,n): # ამ პროგრამას მივმართავ როდესაც n - m >=2
    missing_numbers = []
    i=1
    k = n-m+1
    while i < k-1:
       missing_numbers.append(m+i)
       i += 1
    return missing_numbers
# m=8
# n=10
# print(finding_the_missing_numbers(m,n))

def missing_numbers(arr): # [min,max] შუალედს რამდენი მონაცემი აკლია.
     missings = []
     arr.sort()
     print (arr)
     i=0
     while i < len(arr)-1:
        if arr[i+1] - arr[i] > 1:
         missings.extend(finding_the_missing_numbers(arr[i],arr[i+1]))
         i = i+1
        if arr[i+1] - arr[i] <= 1:
         i = i+1
        if i ==  len(arr)-1:
         return missings
         
import random 
x=[i for i in range(1,31)]
random.shuffle(x)
counter_delete = 5
i=0
while i < counter_delete:
    x.pop()
    i += 1
print("The list of missing numbers is", missing_numbers(x))