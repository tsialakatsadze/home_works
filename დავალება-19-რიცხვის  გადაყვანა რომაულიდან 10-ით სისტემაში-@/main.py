# კლასების დახმარებით დაწერეთ რომაული რიცხვის მთელ რიცხვად გადაქცევის მეთოდი.

# რომაული ციფრები და შესაბამისი მთელი მნიშვნელობებია I=1,V=5,X=10,L=50,C=100,D=500,M=1000.

# რომაულ ჩანაწერს თავისი წესები აქვს
# I=1, II=2, III=3, IV=4, V=5, VI=6, VII=7, VIII=8, IX=9, X=10, 
# XX=20, XXX=30, XL=40, L=50, LX=60, LXX=70, LXXX=80, XC=90, C=100,
# CC=200, CCC=300, CD=400, D=500, DC=600, DCC=700, DCCC=800, CM=900, M=1000. 

# შენიშვნა:CM,CD,XC,XL,IX,IV შესაკრებები ან საერთოდ არ უნდა დავწეროთ, ან უნდა დავწეროთ მხოლოდ ერთხელ.

# მაგალითები:
# 2748 = 2000 + 700 + 40 + 8 = MM + DC + XL + VIII
# 2950 = 2000 + 900 + 50 = MM + CM + L
# 999 = 900 + 90 + 9= CM + XC + IX
# 6724 = 6000 + 700 + 30 + 4= MMMMMM + DCC + XX + IV

class Roman_to_Arabic:
    def __init__(self,text):
        self.text=text
    def roman_numb(self):
        coM = self.text.count("M")   # პასუხობს შეკითხვას რამდენჯერ მოთავსდება 1000 მოცემულ რიცხვში
        coCM = self.text.count("CM") # =1 ან =0 
        coD = self.text.count("D")
        coCD = self.text.count("CD") # =1 ან =0
        coC = self.text.count("C")
        coXC = self.text.count("XC") # =1 ან =0
        coL = self.text.count("L")  
        coXL = self.text.count("XL") # =1 ან =0
        coX = self.text.count("X")
        coIX = self.text.count("IX") # =1 ან =0
        coV = self.text.count("V")
        coIV = self.text.count("IV") # =1 ან =0
        coI = self.text.count("I")   # ბოლოში იწერება მაქსიმუმ 3 ცალი
        if coCM > 1 or coCD > 1 or coXC > 1 or coXL > 1 or coIX > 1 or coIV > 1:
           return "რიცხვის რომაული ჩანაწერი კორექტირებას მოითხოვს"
        elif coD > 2 or coC > 4 or coL > 2 or coX > 4 or coV > 2 or coI > 4:
           return "რიცხვის რომაული ჩანაწერი კორექტირებას მოითხოვს" 
        else:
            arabic_number=coM*1000 + coD*500 + coC*100 + coL*50 + coX*10 + coV*5 + coI
            correction = 2*(coCM*100 + coCD*100 + coXC*10 + coXL*10 + coIX + coIV)
            arabic_number -= correction
            return arabic_number 
             
roman_1 = Roman_to_Arabic("MMCML") # 2950 
print(roman_1.roman_numb()) 
roman_2 = Roman_to_Arabic("CLVII") # 157 
print(roman_2.roman_numb())
roman_3 = Roman_to_Arabic("CMXCIX") # 999
print(roman_3.roman_numb())
roman_4 = Roman_to_Arabic("MMMMMMDCCXXIV") # 6724 
print(roman_4.roman_numb())
roman_5 = Roman_to_Arabic("MMCDCDXXIV") # რიცხვის რომაული ჩანაწერი კორექტირებას მოითხოვს (CD ორჯერ).
print(roman_5.roman_numb()) # 1000+1000+400+400+10+10+4=2824=2000+800+20+4=MM+DCCC+XX+IV
roman_6 = Roman_to_Arabic("MMDCCCXXIV") # 2824
print(roman_6.roman_numb()) 
roman_7 = Roman_to_Arabic("DDDCCCXIX") # რიცხვის რომაული ჩანაწერი კორექტირებას მოითხოვს
print(roman_7.roman_numb()) # 500+500+500+100+100+100+10+9=1000+800+10+9=MDCCCXIV=1819
roman_8 = Roman_to_Arabic("MDCCCXIV") # 1819
print(roman_8.roman_numb()) 
