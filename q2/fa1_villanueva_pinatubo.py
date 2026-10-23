class Publication:
    title:str
    author:str
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
        
    def get_title(self):
        return self.__title
        
    def get_author(self):
        return self.__author
        
    def set_title(self,title):
        self.__title = title

    def set_author(self,author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication):
    number_of_pages:int
    def __init__(self,title,author,number_of_pages):
        super().__init__(title,author)
        self.__number_of_pages = number_of_pages
        
    def get_number_of_pages(self):
        return self.__number_of_pages
        
    def set_number_of_pages(self,number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive")
    
    def display_info(self):
        super().display_info()
        print("Number of pages:")
            
class Magazine(Publication):
    issue_number:int
    def __init__(self,title,author,issue_number):
        super().__init__(title,author)
        self.__issue_number = issue_number
        
    def get_issue_number(self):
        return self.__issue_number
        
    def set_issue_number(self,issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive")
            
    def display_info(self):
        super().display_info()
        print("Issue number:")
        
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)
pub2 = Publication("Bahaghari", "Various Authors")
book2 = Book("El Filibusterismo", "Jose Rizal", 279)
mag2 = Magazine("Vogue", "Various Authors", 67)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information")
mag1.display_info()
print(mag1.get_issue_number())

print("Publication Information:")
pub2.display_info()

print("\nBook Information:")
book2.set_number_of_pages(-310)
book2.display_info()
print(book2.get_number_of_pages())

print("\nMagazine Information")
mag2.display_info()
print(mag2.get_issue_number())
