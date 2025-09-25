class book :
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) is available."
        else:
            return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) is checked out."
        
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"You have returned '{self.title}'."
        else:
            return f"'{self.title}' was not checked out."
        
book1 = book("1984", "George Orwell", "1234567890")
book2 = book("To Kill a Mockingbird", "Harper Lee")
    
print(book1.check_out())
print(book1.return_book())
print(book2.check_out())