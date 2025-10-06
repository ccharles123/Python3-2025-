class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado con éxito")
        else:
            print(f"El libro {self.title} no está disponible, ya fue prestado")
    
    def returnBook(self):
        if not self.available:
            self.available = True
            print(f"Ingresado el libro {self.title} como disponible a la libreria")
        else:
            print(f'El libro {self.title} ya se encuentra como disponible en la libreria') 
    

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"EL libro {book.title} no se encuentra disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.returnBook()
            self.borrowed_books.remove(book)
            print(f"Libro {book.title} fue devuelto")
        else:
            print(f"EL libro {book.title} No esta en la lista de prestados")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} fue agregado al listado de libros disponibles")

    def register_user(self, user):
        self.users.append(user)
        print(f"El Usuario {user.name} fue agregado al listado de usuarios")

    def show_available_books(self):
        print(f"los libros dispobibles son:")
        for book in self.books:
            if book.available:
                print(f"Libro {book.title} autor {book.author}")

# Crear una biblioteca, libros y un usuario
lib = Library()
b1 = Book("Cien años de soledad", "Gabriel García Márquez")
b2 = Book("El Principito", "Antoine de Saint-Exupéry")
u1 = User("Carlos", 101)

lib.add_book(b1)
lib.add_book(b2)
lib.register_user(u1)

lib.show_available_books()     # Muestra ambos

u1.borrow_book(b1)             # Presta "Cien años de soledad"
lib.show_available_books()     # Ya no debería salir b1, solo b2

u1.return_book(b1)             # Devuelve b1
lib.show_available_books()     # Vuelven a aparecer ambos
