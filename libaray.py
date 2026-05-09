# Books and Users
books = {
    1: ["To Kill a Mockingbird", "Harper Lee", 5],
    2: ["1984", "George Orwell", 8],
    3: ["The Great Gatsby", "F. Scott Fitzgerald", 4],
    4: ["Pride and Prejudice", "Jane Austen", 6],
    5: ["The Catcher in the Rye", "J.D. Salinger", 7],
    6: ["The Hobbit", "J.R.R. Tolkien", 10],
    7: ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 12],
    8: ["The Alchemist", "Paulo Coelho", 9],
    9: ["The Lord of the Rings", "J.R.R. Tolkien", 3],
    10: ["Atomic Habits", "James Clear", 11]
}

users = {
    1: {"name":"srinu",'book_id':[1,3,8]},
    2: {"name":"babu",'book_id':[1,3,7]}
}


# person class
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        return f"My book {self.id} and {self.name}"
    

# book class
class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author

# user class
class User(Person):
    def __init__(self, id, name)
        super().__init__(id, name)
        
# admin class
class Admin(Person):
    def __init__(self, id , name)
        super().__init__(id, name)

    
    def add_book(self, book_obj:Book, quantity:int):
        if book_obj.id not in books:
            Book[book_obj.id] = [book_obj.name, book_obj.author, quantity]
            return f"{book_obj.name} added successfully"
        else:
            return f"book id already excited"
        
    # add user to library
    def add_user(self, user_obj:User):
        if user_obj not in users:
            users[user_obj.id] = {"name": user_obj.name, 'books_id':[]}
            return "User added successfully"
        # if user already exsists
        return "User if already exsists"
    

    def delete_book(self, book_id):
        if book_id in books:
            # deleting book from books
            books.pop(bookid)
            return f"Book is {book_id} removed succesfully"
        else: # if bookid not present in books
            return "Book id not found"
        

    def barrow_book(self, user_id, *book_ids):
        if userid in users:
            avaialable_book = []
            notavaialable_book = []
            for book_id in bookids:
               if bookid in books:
                   qunanity = books[bookid][2]
                   if quantity > 0:
                       # updating qunatity 
                       books[bookid][2] -= 1
                       # add book to users 
                       users[userid]['book_id'].append(bookid)
                       aviablable_books.appen({bookid:books[book_id][0]})
               else:
                        anavialable_books.append({bookid:books[bookid][0]})
            return f"Avialable books are :{avialable_books} and unavialable books are :{anvaialable_book}"avaialable_book  
            return "User not found"
        

    def return_book(self, user_id, book_id):
        if userid in users:
           for book_id in books:
                if bookid in books and users[userid]['books_id']:
            
                 # updating qunatity 
                       books[bookid][2] -= 1
                       # add book to users 
                       users[userid]['book_id'].append(bookid)
                return f"All books returned succesfully"
        return "User not found"

    def all_book(self):
        for id, details in books.items():
            print(f"ID: {id}, Name: {details[0]}, Author: {details[1]}, Qty: {details[2]}")

       

    def total_user(self):
        return len(users)
    
# main
if __name__=="__main__":
    print("Welcome to the library")
    admin = Admin(1,"Harper")
    while True:
        print("Select Your opeartion: 1. Add book \n 2. Register User \n 3. Barrow Books \n 4. Return Books \n 5. View All Books \n 6. Total Users \n 8. Exist From Library")
        choice = int(input("Enter you choice:"))
        if choice == 1:
            bookid = int(input("Enter Book_id"))
            book_name = input("Enter Book Name:")
            author = input("Enter Author name:")
            stock = int(input("Enter The book quantity:"))
            # creating books object
            book_obj = Book(id=bookid, name=book_name, author=author)
            # add this book into library
            print(admin.add_book(book_obj=book_object,quantity=stock))
        elif choice == 2:
            userid = int(input("Enter User id:"))
            username = intput("Enter Username")
            # creating user object
            useer_object = user(id=userid, name=username)
            # add user into library users
            print(admin.add_user(user_obj=user_object))
        elif choice == 3:
            print("Your selected option is 3. Barrow Books")
            userid = int(input("Enter User id:"))
            book_ids = lists(map(int, input("enter books ids:").split()))
            print(admin.barrow_book(userid,*book_ids))
        elif choice == 4:
            print("Your selected option is 3. Return Books")
            userid = int(input("Enter User id:"))
            book_ids = lists(map(int, input("enter books ids:").split()))
            print(admin.return_book(userid,*book_ids))
        elif choice == 5:
            print("Your selected option is 5. View All Books")
            all_books = admin.all_book()
            print(f"Book Id  Book Name  , Author Name   quanity")
            for bookid, details in all_books.items():
                print(f"{bookid}  {details[0]}  {deatils[1]}  {details[2]}")
        elif choice == 6:
            print("Your selected optim is 6. Total Users")
            print(admin.total_users())
        elif choice == 7:
            print("Your selected option is :7. Delete Book")
            bookid = int(input("Enter Bookid:"))
            print(admin.delete_book(bookid=bookid))
        elif choice == 8:
            print("Your selected optim is:8. Exsit")
            print("Bye, Your excited from library")
            break
        else:
            print("Invalid choice, Enter the choice in between (1-8)")

                     



