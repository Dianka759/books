from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask_app.models import favorite

class Book:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author = {};


    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for one_book in results:
            books.append( cls(one_book) )
        return books


    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title) VALUES (%(title)s);"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def books_with_authors(cls):
        query = "SELECT * FROM books LEFT JOIN authors on author_id = authors.id;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for row in results:
            book = cls(row)
            author_data = {
                "id":row["authors.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "created_at":row["authors.created_at"],
                "updated_at":row["updated_at"]
            }
            book.author = author.Author(author_data)
            books.append(book)
            
        return books

    @classmethod
    def get_all_favorites(cls,data):
        query = "select * from favorites LEFT JOIN authors ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE author_id=%(id)s"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def save_faves(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    
    @classmethod
    def get_all_favorite(cls,data):
        query = "select * from favorites LEFT JOIN authors ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE book_id=%(id)s"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def get_one_book(cls,data):
        query = "SELECT * FROM books WHERE id=%(id)s;"
        return connectToMySQL('books_schema').query_db(query,data)
