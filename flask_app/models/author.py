from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask_app.models import favorite

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for one_author in results:
            authors.append( cls(one_author) )
        return authors

    @classmethod
    def get_one_author(cls,data):
        query = "SELECT * FROM authors WHERE id=%(id)s;"
        return connectToMySQL('books_schema').query_db(query,data)


    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    



