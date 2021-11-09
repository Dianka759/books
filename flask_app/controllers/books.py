from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite

@app.route('/')
def index():
    return redirect('/authors')

# ==============================================================
#  AUTHORS
# ==============================================================

@app.route("/authors")
def authors():
    all_authors = Author.get_all()
    return render_template("author_page.html", all_authors=all_authors)


@app.route("/create_author", methods=["POST"])
def new_author():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"]
    }
    author = Author.get_all()
    session["author_id"] = author.id
    Author.save(data)
    return redirect("/authors")

@app.route("/author/<int:id>")
def show_author(id):
    data = {
        "id":id
    }
    author = Author.get_one_author(data)
    favorites = Book.get_all_favorites(data)
    books = Book.get_all_books()
    return render_template("author_favorites.html", author=author, favorites=favorites, books=books)

@app.route("/add_to_faves/<int:author_id>", methods=["POST"])
def add_to_faves(author_id):
    data = {
        "author_id":author_id,
        "book_id":request.form["book_id"],
    }
    Author.get_all()
    Book.save_faves(data)
    return redirect(f"/author/{author_id}")

# ==============================================================
#  BOOKS
# ==============================================================

@app.route("/books")
def books():
    all_books = Book.get_all_books()
    return render_template("book_page.html", all_books=all_books)

@app.route("/create_book", methods=["POST"])
def create_book():
    data = {
        "title":request.form["title"],
    }
    Book.save(data)
    return redirect("/books")

@app.route("/book/<int:id>")
def show_book(id):
    data = {
        "id":id
    }
    book = Book.get_one_book(data)
    favorites = Book.get_all_favorite(data)
    authors = Author.get_all()
    return render_template("book_favorited.html", authors=authors, favorites=favorites, book=book)

@app.route("/add_book_to_faves/<int:book_id>", methods=["POST"])
def add_book_to_faves(book_id):
    data = {
        "book_id":book_id,
        "author_id":request.form["author_id"],
    }
    Book.get_all_books()
    Book.save_faves(data)
    return redirect(f"/book/{book_id}")

