#Model Layer Borrowing Records

# Import database operation tool class
from  mysqlUtils import MysqlUtils

# Record bean class
class record(object):
    def __init__(self,book_id,book_name,location,borrow_stu_name,borrow_time):
        self.book_id=book_id
        self.book_name=book_name
        self.location=location
        self.borrow_stu_name=borrow_stu_name
        self.borrow_time=borrow_time

# Record bean class
class recordModel(object):
    def get_record_data(self):
        self.util =MysqlUtils('34.147.132.176','demo','fcsummer123456','library','utf8') # X_Change
        # self.util =MysqlUtils('114.115.163.29', 'root', 'kun20021127', 'library', 'utf8') # X_Change
        self.u = self.util.query_borrowrecord()
        record_list = []
        for i in self.u:
            record_list.append(record(i[0], i[1], i[2], i[3], i[4]))
        return record_list
