
# დავალება
# დაწერეთ ფუნქცია რამოდენიმე  ფუნქცია სადაც შევძლებთ ახალი წიგნის, ავტორის და გამომცემლობის დამატებას.
# მოძებნას ავტორით და წიგნით:

# "ლევან გოთუა", "გმირთა ვარამი", "პალიტრა ლ"
# "მაინ რიდი", "უთავო მხედარი", "პალიტრა ლ"


keys=["author","book", "publishing_house"]
values=[
    ["ილია ჭავჭავაძე","საბავშვო ლიტერატურის საგანძური","საქართველოს მაცნე"],
    ["ვაჟა ფშაველა", "მოთხრობები", "ელფის გამომცემლობა"],
    ["ოტია იოსელიანი","დაჩის ზღაპრები","საქართველოს მაცნე"],
    ["მიხეილ ჯავახიშვილი","ჯაყოს ხიზნები", "ელფის გამომცემლობა"],
    ["იაკობ გოგებაშვილი", "მოთხრობები პატარებისათვის", "ელფის გამომცემლობა"],
    ["გურამ დოჩანაშვილი", "სამოსელი პირველი", "მერიდიანი"]
]
old_dict=dict(zip(keys,zip(*values)))

def add_new_author(new):
    new_author = input("შემოიტანეთ ავტორის სახელი და გვარი: ")
    new_book = input("შემოიტანეთ წიგნის დასახელება: ")
    new_publishing_house = input("შემოიტანეთ გამომცემლობის დასახელება: ")
    new.append(new_author)
    new.append(new_book)
    new.append(new_publishing_house)
    return new

def changes_in_the_dictionary(keys,values,k): # k არის დასამატებელი ავტორების რაოდენობა
    i=0
    while i < k:
        new=[]
        values.append(add_new_author(new))
        new_new_dict=dict(zip(keys,zip(*values)))
        i += 1
        if i == k:
          return new_new_dict

new_dict = changes_in_the_dictionary(keys,values,3)
print(new_dict)
print(new_dict["author"])
print(new_dict["book"])





