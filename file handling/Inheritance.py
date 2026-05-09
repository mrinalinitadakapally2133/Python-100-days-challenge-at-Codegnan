# parent class with implementation and without child implementation
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def details(self):
        return f"My name is {self.username}, email_id is {self.email} and {self.age} years old"
# class admin
class admin(User):
    def __init__(self, username:str, email:str, password:str, total_users:int):
        self.username = username
        self.email = email
        self.password = password
        self.total_users = total_users
    def total_users(self):
         return f"I am working as admin and user are{self.total_users}"

u1 = User(username =" babu", email = "babu@gmail.com", password = "babu123")
a1 = admin(username="srinu", email= "srinu@gmail.com", password = "srinu@123", total_users=100)
print("User details is:", u1.username)
print("admin details is:", a1.username)
print(a1.show())
a1.age = 30
print("admin details is:", a1.deatils())