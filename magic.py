#magic methods

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} : {self.author} : {self.num_pages}"
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return self.num_pages + other.num_pages

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
book1 = Book("Mindest","Dr Carlos Dweck",301)
book2 = Book("Deep Work","No idea",234)

print(book1)
print(book2)

print(book1 < book2)
print(book1 + book2)
print(book1["title"])
print("Deep" in book2)