#Model layer Reader information

# Import database operation tool class
from  mysqlUtils import MysqlUtils

#Reader bean class
class reader(object):
    def __init__(self,reader_name,reader_class,reader_learn_num,reader_phone,reader_borrow_num):
       self.reader_name=reader_name
       self.reader_class=reader_class
       self.reader_learn_num = reader_learn_num
       self.reader_phone = reader_phone
       self.reader_borrow_num = reader_borrow_num

#Readermodel class
# Properties：
class readerModel(object):

    def get_reader_data(self):
        self.util =MysqlUtils('34.147.132.176','demo','fcsummer123456','library','utf8')
        self.u = self.util.query_readerinfor()
        recoder_list = []
        # num = self.u.count()
        index=0
        for i in self.u:
            recoder_list.append(reader(i[0], i[1], i[2], i[3], i[4]))
        return recoder_list










