
# დავალება(მე-15 ლექციისთვის ამ პროგრამის მისამართის გადაგზავნა).
# დაწერეთ ფუნქცია პითონში, ტექსტურ ფაილში მაღალი რეგისტრში  არსებული 
# წინადადებების  დასათვლელად.
# list_2 = ['red', 'Green', 'white', 'Black', 'Pink', 'Yellow']

list_2 = open("text2.txt","w")
list_2.writelines(['red\n', 'Green\n', 'white\n', 'Black\n', 'Pink\n', 'Yellow\n'])
list_2.close()

def upper_is(word):
    if word[0] == word[0].upper():
        upper_is = True
    else:
        upper_is = False
    return upper_is
def uppers_count(lst):
    count=0
    i=0
    while i < len(lst):
        if upper_is(lst[i]) == True:
            count += 1
            i += 1
        else:
            i += 1
    return count


read_words = open("text2.txt", "r")
lst=read_words.readlines()
print(lst)
print(uppers_count(lst))





