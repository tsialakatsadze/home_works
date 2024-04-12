
# 1.	დაწერეთ პროგრამა, რომელიც იღებს სტრიქონს, როგორც შეყვანას და აბრუნებს True-ს, თუ ის პალინდრომია 
# (პალინდრომი არის ისეთი ტექსტი, რომელიც მარცხნიდანაც და მარჯვნიდანაც ერთნაირად იკითხება), 
# თუ არა მაშინ False. მაგალითად, თუ შევიყვანთ "level", ფუნქციამ უნდა დააბრუნოს True.
# მაგალითები: "აირევი ივერია", 12345677654321, 123454321, "palindromic words".

# text=str(input())
# l = len(text)
# n = int(l/2)
# left = text[0:n]
# right = text[l-1:l-n-1:-1]
# print("Is the string a polyndrome?")
# if left == right:
#      print(True)  
# else:
#      print(False)

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ტექსტი,
# ტექსტის სიმბოლოები გადაყავს შესაბამის ASCII სტანდარტში და გვიბეჭდავს ამ რიცხვების თანმიმდევრობას  
# მითითება: შეიტანეთ 1) 123,  2) საქართველო, 3) Georgia

name = str(input())

enC=name.encode("utf-8", errors="ignore")
print("# შემოტანილ ინფორმაციას კითხულობს utf-8 კოდში.")
print(enC)

deC=enC.decode("utf-8", errors="ignore")
print("# ახდენს utf-8 კოდში ჩაწერილის დეკოდირებას.")
print(deC)

enCAscii=name.encode("ascii", errors="ignore")
print("# გაითვალისწინეთ: არსებობს ცხრილი, რომელშიც ჩანს, თუ რისი ჩაწერაა შესაძლებელი ASCII სტანდარტში.")

print("# შემოტანილ ინფორმაციას კითხულობს, ან ვერ კითხულობს ASCII სტანდარტში.")
print(enCAscii)

deCAscii=enCAscii.decode("ascii", errors="ignore")
print("# გაითვალისწინეთ: თუ ვერ მოხერხდა მოცემულის ASCII -ში ჩაწერა, მაშინ დეკოდირებაც ვერ მოხერხდება.")
print("# ახდენს ASCII კოდში ჩაწერილის დეკოდირებას.")
print(deCAscii)

