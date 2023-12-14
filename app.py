# MVC pattern
# controller layer

from flask import Flask, render_template, flash, request, abort, redirect, url_for
# from models import User
#Import database operation tool class
from  mysqlUtils import MysqlUtils
#Import json package
import json

#MVC pattern model layer
from models.readerModel import readerModel
from models.recordModel import recordModel
from models.bookModel import bookModel
# MysqlUtils('114.115.163.29','root','kun20021127','library','utf8')
util=MysqlUtils('34.147.132.176', 'demo', 'fcsummer123456', 'library', 'utf8') # X_Change
#All book information
# u=util.query_all_book()

app = Flask(__name__)
app.secret_key = '123'#flash encryption

@app.route('/')
def hello_world():
    flash("")  # Login registration prompt information
    content = "hello world"
    # return render_template("login.html", content=content)
    return render_template("login.html", content=content)

# register
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        form = request.form
        username = form.get('username')
        password = form.get('password')
        password2 = form.get('password2')
        # The front end completes judging whether the content is empty
        if not username:
            flash("Please enter user name")
            return render_template("register.html")
        if not password:
            flash("Please enter password")
            return render_template("register.html")
        if not password2:
            flash("Please enter the confirmation password")
            return render_template("register.html")
        if not password == password2:
            flash("Two passwords are inconsistent")
            return render_template("register.html")
        else:# The registration information is correct and written to the database.
            util.register_Admin(username, password)
            flash("registration success")
            return render_template("register.html")
    else:
        return render_template("register.html")


# Login interface routing
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        form = request.form
        username = form.get('username') + ""
        password = form.get('password') + ""
        if not username:
            flash("please enter user name")
            return render_template("login.html", password=password)
        if not password:
            flash("Please enter password")
            return render_template("login.html", username=username)
        password2 = util.query_Password(username) # Password query based on account
        if (password == password2):
            return render_template("addbook.html")
        else:
            flash("wrong user name or password")
            return render_template("login.html", username=username, password=password)
    else: #When the request method is GET
        return render_template("login.html")

@app.route('/addbook', methods=['POST', 'GET'])
def addbook():
    if request.method == "POST":
        form = request.form
        number = form.get('number') + ""
        name = form.get('bookname') + ""
        author = form.get('author') + ""
        publicationdate = form.get('pdate') + ""
        location = form.get('address') + ""
        remark = form.get('description') + ""
        if not number:
            flash("Please enter id")
            return render_template("addbook.html", number=number)
        if not name:
            flash("Please enter the book title")
            return render_template("addbook.html", number=number,name=name)
        if not location:
            flash("Please enter location")
            return render_template("addbook.html", number=number,name=name,location=location)
        m = bookModel()
        m.add_book(number,name,author,publicationdate,location,remark)
        flash("Book added successfully")
        return render_template("addbook.html")
    else:
        return render_template("addbook.html")

# Delete book interface
@app.route('/deletebook', methods=['GET','POST'])
def deletebook():
    # u = util.query_all_book()
    #MVC pattern refactoring
    m = bookModel()
    books = m.get_all_book_data()
    return render_template("deletebook.html", books=books)

#Route responsible for deleting books with parameters: book name
@app.route('/deletebook2/<bookid>', methods=['GET'])
def deletebook2(bookid):
    #Delete the selected books first and then query
    m = bookModel()
    m.delete_one_book_by_id(bookid)
    books = m.get_all_book_data()
    flash(bookid)
    return render_template("deletebook.html", books=books)

# Modify book interface
@app.route('/changebook', methods=['POST', 'GET'])
def changebook():
    # u = util.query_all_book()
    # MVC pattern refactoring
    m = bookModel()
    books = m.get_all_book_data()
    return render_template("changebook.html", books=books)

# Modify book interface detailed interface
@app.route('/changebookinfor/<bookid>', methods=['POST', 'GET'])
def changebookinfor(bookid):
    detail=util.query_one_book_byid(bookid)
    if request.method == "POST":
        form = request.form # If you click Modify, delete first and then add.
        number = form.get('number') + ""
        name = form.get('bookname') + ""
        author = form.get('author') + ""
        publicationdate = form.get('pdate') + ""
        location = form.get('address') + ""
        remark = form.get('description') + ""
        if not number:
            flash("Please enter id")
            return render_template("changebookinfor.html")
        if not name:
            flash("Please enter the book title")
            return render_template("changebookinfor.html", number=number)
        if not location:
            flash("Please enter location")
            return render_template("changebookinfor.html", number=number,name=name)
        util.delete_book(bookid)
        util.add_book(number, name, author, publicationdate, location, remark)
        flash("Book modified successfully")
        return render_template("changebookinfor.html",detail=detail)
    else:
        return render_template("changebookinfor.html",detail=detail)

@app.route('/querybook', methods=['POST', 'GET'])
def querybook():
    m = bookModel()
    if request.method == "POST":
        name = request.values.get('bookname').strip()

        # Use LIKE query
        if name:
            # Constructing a LIKE query string
            like_string = f"%{name}%"
            onebook = m.get_books_like_name(like_string)
        else:
            onebook = m.get_all_book_data()

        return render_template("querybook.html", books=onebook, name=name)
    else:
        books = m.get_all_book_data()
        return render_template("querybook.html", books=books)
        
#Book borrowing information interface
@app.route('/borrowrecord', methods=['POST', 'GET'])
def borrowrecord():
    # u = util.query_borrowrecord()
    # MVC pattern refactoring
    m = recordModel()
    records = m.get_record_data()
    return render_template("borrowrecord.html", records=records)

#Reader information information interface
@app.route('/readerinfor', methods=['POST', 'GET'])
def readerinfor():
    # u = util.query_readerinfor()
    #MVC pattern refactoring
    m=readerModel()
    readers=m.get_reader_data()
    return render_template("readerinfor.html", readers=readers)


# Error interface (exception handling)
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

def create_app():
   return app

if __name__ == '__main__':
    # from waitress import serve # X_Change

    # serve(app, host="0.0.0.0", port=8721) # X_Change
    app.run("0.0.0.0",8721) # X_Change
