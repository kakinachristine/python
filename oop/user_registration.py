class User:
    def __init__(self,name,email,password):
        self.userName = name
        self.userEmail = email
        self.userPassword = password
    def logout(self):
        print("Yeah, i can log out")
user1 = User("king","king@gmail.com","king123")
user2 = User("adrian","adrian@gmail.com","adrian123")
user3 = User("kiki","kiki@gmail.com","kiki123")
user4 = User("mjomba","mjomba@gmail.com","mjomba123")
print(user3.userEmail)
user4.logout()
user1.logout()

class Admin(User):
    def suspend(self):
        print("yeah, i can suspend students")
user5 = Admin("emobilis","emobilis@gmail.com","emobilis123")
user5.logout()
user5.suspend()
