
### **Chapter I：前端设计**

![img](./static/images/login.png) 

表 1登录界面

![img](./static/images/register.png) 

表 2注册界面

![img](./static/images/add.png) 

表 3添加书籍

![img](./static/images/delete.png) 

表 4删除书籍

![img](./static/images/update.png) 

表 5修改书籍

 

![img](./static/images/query.png) 

表 6查找书籍

![img](./static/images/record.png) 

表 7借阅记录

![img](./static/images/info.png) 

表 8读者信息

### **第二章：数据库设计**

#### **4.1 **数据表的设计及部分初始数据的输入



表1  book书籍信息表

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