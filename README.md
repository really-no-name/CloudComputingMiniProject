
### **Chapter I：Front-end design**

![img](./static/images/login.png) 

Table 1 Login interface

![img](./static/images/register.png) 

Table 2 Registration interface

![img](./static/images/add.png) 

Table 3 Add books

![img](./static/images/delete.png) 

Table 4 Delete Books

![img](./static/images/update.png) 

Table 5 Modify Books

 

![img](./static/images/query.png) 

Table 6 Find Books

![img](./static/images/record.png) 

Table 7 Borrowing records

![img](./static/images/info.png) 

Table 8 Reader information

### **Chapter 2: Database Design**

#### **4.1 **Design of data table and input of some initial data



Table 1 book information table

| 字段名称        | 数据类型 | 默认值 | 长度 | 说明                       |
| --------------- | -------- | ------ | ---- | -------------------------- |
| ID              | Int      | 无     | 4    | 数据Id值                   |
| Name            | Varchar  | 无     | 20   | 书名                       |
| Number          | Varchar  | 无     | 8    | 书籍序列号                 |
| Author          | Varchar  | 无     | 10   | 作者                       |
| Publicationdate | Date     | 无     | 10   | 出版时间                   |
| Isborrow        | Int      | 无     | 1    | 借阅状态(1:被借，0:未被借) |
| Remark          | Varchar  | 无     | 50   | 图书简介                   |
| Location        | Varchar  | 无     | 20   | 书籍地点                   |
| Borrowname      | Varchar  | 无     | 20   | 借书人姓名                 |
| Borrowtime      | Date     | 无     | 10   | 借书时间                   |

| Field name      | Data type  | Default value | Length | Description                 |
| --------------- | ---------- | ------------- | ------ | --------------------------- |
| ID              | Int        | None          | 4      | DataId value                |
| Name | Varchar | None | 20 | Book Title |
| Number | Varchar | None | 8 | Book serial number |
| Author | Varchar | None | 10 | Author |
| Publicationdate | Date | None | 10 | Publication date |
| Isborrow | Int | None | 1 | Borrowing status (1: Borrowed, 0: Not borrowed) |
| Remark | Varchar | None | 50 | Book Introduction |
| Location | Varchar | None | 20 | Book Locations |
| Borrowname | Varchar | None | 20 | Borrower name |
| Borrowtime | Date | None | 10 | Borrowing time |

表2  student读者信息表

| 字段名称     | 数据类型 | 默认值 | 长度 | 说明     |
| ------------ | -------- | ------ | ---- | -------- |
| ID           | Int      | 无     | 4    | 数据Id值 |
| Name         | Varchar  | 无     | 10   | 读者姓名 |
| Psw          | Varchar  | 无     | 10   | 密码     |
| Class        | Varchar  | 无     | 10   | 班级     |
| Learnnumber  | Varchar  | 无     | 20   | 学号     |
| Phonenumber  | Varchar  | 无     | 20   | 手机号   |
| Borrownumber | Varchar  | 无     | 20   | 借书数量 |

 


表3  user图书管理员信息表

| 字段名称 | 数据类型 | 默认值 | 长度 | 说明       |
| -------- | -------- | ------ | ---- | ---------- |
| ID       | Int      | 无     | 4    | 数据Id值   |
| Name     | Varchar  | 无     | 10   | 管理员姓名 |
| Psw      | Varchar  | 无     | 10   | 密码       |

 


表4  record 结束记录信息表

| 字段名称   | 数据类型 | 默认值 | 长度 | 说明         |
| ---------- | -------- | ------ | ---- | ------------ |
| ID         | Int      | 无     | 4    | 数据Id值     |
| Readername | Varchar  | 无     | 10   | 管理员姓名   |
| Booknumber | Varchar  | 无     | 10   | 密码         |
| Borrowdate | Date     | 无     | 10   | 借书时间     |
| Returndate | Date     | 无     | 10   | 还书时间     |
| Remark     | Varchar  | 无     | 10   | 记录备注信息 |

 

### **第三章：总结**

这个图书馆项目的CURD全部实现，并且前端使用fetch请求REST-API服务接口，进行增删改查，对接GCP-Mysql，进行数据的存储。
