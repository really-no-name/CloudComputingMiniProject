#Import mysql database
import pymysql

class MysqlUtils():
    #initialization
    def __init__(self,host,user,password,db,charset):

        self.host=host
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()

    # #add books
    def add_book(self,number,name,author,publicationdate,location ,remark):
        # Add multiple pieces of data
        # sqlstr="insert into book (number,name,author,publicationdate,location ,remark) values(%s,%s,%s,%s,%s,%s);"
        # data = [
        #     ('"+number+"',''"+name+"' , '"+author+"','"+publicationdate+"','"+location+"','"+remark+"')
        #     # ,
        #     # ('june', '258'),
        #     # ('marin', '369')
        # ]
        # # Splice and execute sql statements
        # self.cur.executemany(sqlstr, data)
        #Add a single piece of data
        sqlstr="insert into book (number,name,author,publicationdate,location ,remark) " \
               "values( '"+number+"','"+name+"','"+author+"','"+publicationdate+"','"+location+"','"+remark+"');"
        self.cur.execute(sqlstr)
        # Pay attention to submission when writing operations are involved
        self.conn.commit()

#Delete books Delete based on book id
        def delete_book(self, bookid):
        sqlstr="delete from book where number = '" + bookid + "';"
        #Splice and execute sql statements
        self.cur.execute(sqlstr)
        # Pay attention to submission when writing operations are involved
        self.conn.commit()

    # #Modify books    
    #Delete first and then add to implement the modification function
    # def change_book(self,number,name,author,publicationdate,location ,remark):

    # Find all books
    def query_all_book(self):
        self.cur.execute('SELECT number ,name,author,publicationdate,location ,remark FROM book order by number')
        result = self.cur.fetchall()
        return result

    #Search for specified books (parameter: book title) Search for books based on book names
    def query_one_book(self,name):
        sqlstr="SELECT number ,name,author,publicationdate,location ,remark FROM book WHERE name = '"+name+"'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    # Find the specified book (parameter: book id) Query the book based on the book name
    def query_one_book_byid(self, id):
        sqlstr = "SELECT number ,name,author,publicationdate,location ,remark FROM book WHERE number = '" + id + "'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    # Borrowing record query
    def query_borrowrecord(self):
        sqlstr = "SELECT number ,name,location ,borrowname,borrowtime FROM book WHERE isborrow = 1"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    # Find reader information
    def query_readerinfor(self):
        sqlstr = "SELECT name,class,learnnumber,phonenumber,borrownumber FROM student order by id"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    #Registered administrator (parameters: account number, password)
    def register_Admin(self,uername,password):
        # Add a single piece of data
        sqlstr = "insert into user (username,psw) values( '" + uername + "','" + password + "');"
        self.cur.execute(sqlstr)
        # Pay attention to submission when writing operations are involved
        self.conn.commit()

    #Administrator login (check password through account)
    def query_Password(self,username):
        sqlstr = "SELECT psw FROM user WHERE username='" + username + "'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        for row in result:
            password=str(row[0])
            return password
    def query_LikeBook(self,book_name):
        sqlstr = "SELECT * FROM book WHERE name like '" + book_name + "'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result
