#Library management  

class Book:
        
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def displayInfo(self):
        return "Title: {} ,Author: {}".format(self.title,self.author)
class LibraryBook(Book):#inheritance
    def __init__(self,title,author,copies_available):
        super().__init__(title,author)
        self.copies_available=copies_available
    def borrowBook(self):
        if self.copies_available>0:
            self.copies_available-=1
            return "The book borrowed is {} and copies left are {}".format(self.title,self.copies_available)
        else:
            return "The number of copies available are {}".format(self.copies_available)            
    def returned(self):
        self.copies_available+=1
        return "The book returned is {} and number of copies available now is {}".format(self.title,self.copies_available)
    
book1=LibraryBook("The River and The Source","Margaret Ogolla",20) 
print(book1.displayInfo())  
print(book1.borrowBook())
print(book1.returned())
book2=LibraryBook('The Blossoms of the savanna','Kimani Ngugi',10)
print(book2.borrowBook())


        