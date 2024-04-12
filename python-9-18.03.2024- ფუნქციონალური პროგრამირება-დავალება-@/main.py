
# დავალება 1.
# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით დაგენერირებული ელემენტისგან 
# შემდგარ ლისტს, გამოიყენეთ sort() მეთოდი და sorted() ფუნქცია, 
# დააბრუნეთ დასორტირებული ლისტი ჯერ ზრდადობით და შემდეგ კლებადობით.

# import random
# x=[i for i in range(1,101)]
# random.shuffle(x)

# print(sorted(x))
# print(x) # აქ მოცემული x შეცვლილი არ იქნება

# x.sort()
# print(x) # აქ x უკვე სორტირებული გახდება, ანუ მოცემული x შეიცვლება

# დავალება 2.
# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 
# 100 შემთხვევითობის პრინციპით დაგენერირებული ელემენტისგან შემდგარ ლისტს, 
# გამოიყენეთ ორი სორტირების ალგორითმი(არ აქვს არსებითი მნიშვნელობა, რომელი ალგორითმები იქნება),
# ერთი ალგორითმით დაასორტირეთ ზრდადობით, 
# მეორე ალგორითმით დაასორტირეთ კლებადობით, ორივე შედეგი დაპრინტეთ ტერმინალში. 

def insert_sort(arr):      # ჩემი ვარიანტი
        new_arr=[]
        new_arr.append(arr[0])
        p=False
        i=1
        while i < len(arr):
           insert_in_sorted(new_arr,arr[i])
           i += 1
           if len(new_arr) == len(arr):
              p=True
           if p==True:
              return new_arr

def insert_in_sorted(array,b):    
    min_index = 0
    max_index = len(array)-1
    k=(max_index+min_index)//2
    end_end = False
    while max_index - min_index >= 0:
       k=(max_index+min_index)//2
       if b == array[k]:
          array.insert(k,b)
          end_end = True
       if max_index - min_index == 0 and b<= array[k]:
          array.insert(k,b)
          end_end = True
       if max_index - min_index == 0 and b > array[k]:
          array.insert(k+1,b)
          end_end = True
       if max_index - min_index == 1 and b<= array[k]:
          array.insert(k,b)
          end_end = True
       if max_index - min_index == 1 and  array[k] < b <= array[k+1]:
          array.insert(k+1,b)
          end_end = True
       if max_index - min_index == 1 and  array[k+1] < b:
          array.insert(k+2,b)
          end_end = True
       if b > array[k]:
          min_index = k+1
       if b < array[k]:
          max_index = k-1 
       if end_end == True:
          return array

                             #  რევერსი Bubble მეთოდით (ჩემი დაწერილი)
def reverse_bubble(array):
    l=len(array)
    i=0
    k=l-1
    while i < k:
          if array[i] < array[i+1]:
           array[i],array[i+1]=array[i+1],array[i]
           i += 1
          else:
           i +=1
          if i==k and k>1:
             k -= 1 
             i=0
    return(array)




import time                
import random

for_insert_sort=[i for i in range(1,101)]
random.shuffle(for_insert_sort)

start = time.time()                              #  insert_sort
print(insert_sort(for_insert_sort))
print(time.time()-start) 

for_bubble_sort=[i for i in range(1,101)]
random.shuffle(for_bubble_sort)

start = time.time()                              # reverse_bubble
print(reverse_bubble(for_bubble_sort))
print(time.time()-start) 


