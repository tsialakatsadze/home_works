
# დავალება -17-
# 1. მომხმარებლის კლასი:
# - ინიციალიზდება მომხმარებლის სახელით, ცარიელი ლისტით პოსტებისთვის 
#                                        და ცარიელი სეტით მეგობრებისთვის.
# - მეთოდები მოიცავს პოსტის შექმნას, პოსტის კომენტარებს, პოსტის მოწონებას.
# 2. პოსტის კლასი :
# - ინიციალიზებულია შინაარსით, ავტორით, კომენტარების სიით, მოწონებების სიით 
# - მეთოდები მოიცავს კომენტარის დამატებას და მოწონების დამატებას.
# 3. კომენტარების კლასი:
# - ინიციალიზებულია შინაარსით და ავტორით.
# 4. გამოყენება:
# - ქმნის ორ მომხმარებელს, ამეგობრებს მათ.
# - User1 ქმნის პოსტს, User2 კომენტარს აკეთებს მასზე და User1 ალაიქებს კომენტარს.
# - User1 ქმნის სხვა პოსტს და User2 ალაიქებს.

class User:
    def __init__(self):
        self.post=[]
        self.comment=[]
        self.likes=[]
        self.friends=[]
    def add_post(self,post):
        self.post.append(f"{post}")
        print(f"{self.post}")
    def add_comment(self,comment):
        self.comment.append(f"{comment}")
        print(f"{self.comment}")
    def add_likes(self,likes):
        self.likes.append(f"{likes}")
        print(f"{self.likes}")
    def add_friends(self,friends):
        self.friends.append(f"{friends}")
        print(f"{self.friends}")

friends_siko = User()
friends_siko.add_friends("Niko agreed to be your friend")
post_siko = User() 
post_siko.add_post("siko: ძალა ერთობაშია")
likes_niko = User()
likes_niko.add_likes("niko: siko: like")
post_niko = User()
post_niko.add_post("niko: გაერთიანებულ საქართველოს ვერავინ ვერ მოერევა")
likes_niko = User()
likes_niko.add_likes("siko: niko: like")