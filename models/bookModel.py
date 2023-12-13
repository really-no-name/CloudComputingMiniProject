#Model层

#导入数据库操作工具类
from  mysqlUtils import MysqlUtils

#书籍bean类 属性number name author publiccationdate location remark
class book(object):
    def __init__(self, number ,name,author,publicationdate,location ,remark ):
        self.number = number
        self.name = name
        self.author = author
        self.publicationdate=publicationdate
        self.location=location
        self.remark=remark

#书籍model
class bookModel(object):

    #初始化 建立数据库连接
    def __init__(self):
        self.util = MysqlUtils('34.147.132.176', 'demo', 'fcsummer123456', 'library', 'utf8')

    #查询所有书籍
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

    #查询一本书
    def get_one_book_data(self,bookname):
        self.u = self.util.query_one_book(bookname)
        one_book = []
        for i in self.u:
            one_book.append(book(i[0], i[1], i[2], i[3], i[4],i[5]))
        return one_book

    #根据id删除一本书
    def delete_one_book_by_id(self,bookid):
        self.util.delete_book(bookid)

    #添加书籍
    def add_book(self,number,name,author,publicationdate,location,remark):
        self.util.add_book(number,name,author,publicationdate,location,remark)


