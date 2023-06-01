class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
    def get_info(self):
        print(f"Назва книги: {self.title},автор: {self.author}")

d=Book("hucdn", "I")
d.get_info()



