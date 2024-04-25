
# დაწერეთ პითონის პროგრამა კლასების გამოყენებით, რომელიც წარმოადგენს კალათას.
# დაწერეთ ნივთების დამატებისა და წაშლის მეთოდები და პროდუქტების ფასის დათვლა.

class ShoppingCart:
       
    def __init__(self):
        self.cart=[]
        self.count=0
        self.total=0
    def add(self,name,numb,price):
        self.cart.append(f"{name} , {numb} , {price}")
        self.count += numb
        self.total += numb*price
        print(f"კალათის შემადგენლობა: {self.cart}")
        print(f"კალათაში არსებული ნივთების რაოდენობა: {self.count}")
        print(f"გადასახდელი თანხა ლარებში: {self.total}")
    def remove(self,name,numb,price):
        self.count -= numb
        self.total -= numb*price
        self.cart.remove(f"{name} , {numb} , {price}")
        print(f"კალათის შემადგენლობა: {self.cart}")
        print(f"კალათაში არსებული ნივთების რაოდენობა: {self.count}")
        print(f"გადასახდელი თანხა ლარებში: {self.total}")
    
shop = ShoppingCart() 
shop.add("კარაქი", 1 , 18.50)
shop.add("პური", 3 , 1.20)
shop.add("ზეთი", 5 , 6.40)
shop.remove("ზეთი", 5 , 6.40)
shop.add("ზეთი", 3 , 6.50)






