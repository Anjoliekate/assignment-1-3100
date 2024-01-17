class Library:

    def __init__(self):
        self.available_list = ['To Kill a Mockingbird', '1984',
                               'The Lord of the Rings', 'Harry Potter', 'The Alchemist']

    def add_book(self, book):
        self.available_list.append(book)
        print(self.available_list)

def main():
    lib = Library()
    book = input("What book would you like to add? ")
    lib.add_book(book)    

if __name__ == "__main__":
    main()