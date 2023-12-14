#Model layer

# Import database operation tool class
from  mysqlUtils import MysqlUtils

#Bookbean Class Attributes number name author publiccationdate location remark
class book(object):
    def __init__(self, number ,name,author,publicationdate,location ,remark ):
        self.number = number
        self.name = name
        self.author = author
        self.publicationdate=publicationdate
        self.location=location
        self.remark=remark

#Bookmodel
class bookModel(object):

    # Initialise Establish database connection
    def __init__(self):
        self.util = MysqlUtils('34.147.132.176', 'demo', 'fcsummer123456', 'library', 'utf8') # X_Change
        # MysqlUtils('34.147.132.176', 'demo', 'fcsummer123456', 'library', 'utf8') # X_Change
        # self.util = MysqlUtils('114.115.163.29', 'root', 'kun20021127', 'library', 'utf8') # X_Change

    #Search All Books
    def get_all_book_data(self):
        self.u = self.util.query_all_book()
        book_list = []
        for i in self.u:
            book_list.append(book(i[0], i[1], i[2], i[3], i[4],i[5]))
        return book_list

    def get_books_like_name(self, like_string):
        self.u=self.util.query_LikeBook(like_string)
        book_list=[]
        for i in self.u:
            book_list.append(book(i[0], i[1], i[2], i[3], i[4], i[5]))
        return book_list

    # Query a book
    def get_one_book_data(self,bookname):
        self.u = self.util.query_one_book(bookname)
        one_book = []
        for i in self.u:
            one_book.append(book(i[0], i[1], i[2], i[3], i[4],i[5]))
        return one_book

    #Delete a book based on id
    def delete_one_book_by_id(self,bookid):
        self.util.delete_book(bookid)

    #add books
    def add_book(self,number,name,author,publicationdate,location,remark):
        self.util.add_book(number,name,author,publicationdate,location,remark)


