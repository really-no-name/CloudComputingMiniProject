# Book Manager

Book Manager is a simple book management system based on Flask and Google Books API. It allows users to search for books, view detailed information, and manage their personal book collections and borrowing information.

## Features
- Search books.
- View book details.
- Manage personal book collection.
- View borrowing information and reader information

## Installation Guide

### Environmental requirements
- Python 3.6+
- Flask

### installation steps

1. **Clone repository**

     ```bash
     git clone https://github.com/really-no-name/CloudComputingMiniProject.git
     cd CloudComputingMiniProject
     ```
    Or use via ssh：
     ```bash
     git clone git@github.com:really-no-name/CloudComputingMiniProject.git
     cd CloudComputingMiniProject
     ```

2. **Install dependencies**

     Run in the project directory:

     ```bash
     pip install -r requirements.txt
     ```

## Run the application

Run in the project directory:

```bash
python3 app.py
```

Visit `http://External IP:8721` to view the application.

## Function Description

- **Search books**: Visit `/querybook` to search for books.
- **Add book to collection**: Send a POST request to `/addbook` to add a book to your collection.
- **Revise book in collection**: Send a PUT request to `/changebook` to update a specific book in your collection.
- **Delete book from collection**: Send a DELETE request to `/deletebook` to remove a book from your collection.

## Architecture

![img](./static/images/architecture.png) 


### **Chapter I：Front-end design**

![img](./static/images/login_en.png) 

Table 1 Login interface

![img](./static/images/register_en.png) 

Table 2 Registration interface

![img](./static/images/add_en.png) 

Table 3 Add books

![img](./static/images/delete_en.png) 

Table 4 Delete Books

![img](./static/images/update_en.png) 
![img](./static/images/update_info_en.png) 

Table 5 Modify Books

![img](./static/images/query_en.png) 

Table 6 Find Books

![img](./static/images/record_en.png) 

Table 7 Borrowing records

![img](./static/images/Info_en.png) 

Table 8 Reader information

### **Chapter 2: Database Design**

#### Design of data table and input of some initial data



Table 1 book information table

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

Table 2 student reader information table

| Field name   | Data type | Default value | Length | Description |
| ------------ | --------- | ------------- | ------ | -------- |
| ID | Int | None | 4 | DataId value |
| Name | Varchar | None | 10 | Reader Name |
| Psw | Varchar | None | 10 | Password |
| Class | Varchar | None | 10 | Class |
| Learnnumber | Varchar | None | 20 | Student number |
| Phonenumber | Varchar | None | 20 | Phone number |
| Borrownumber | Varchar | None | 20 | Number of books borrowed |

 


Table 3 user librarian information table

| Field name | Data type | Default value | Length | Description |
| -------- | -------- | ------ | ---- | ---------- |
| ID | Int | None | 4 | DataId value |
| Name | Varchar | None | 10 | Administrator Name |
| Psw | Varchar | None | 10 | Password |

 


Table 4 record end record information table

| Field name | Data type | Default value | Length | Description |
| ---------- | -------- | ------ | ---- | ------------ |
| ID | Int | None | 4 | DataId value |
| Readername | Varchar | None | 10 | Administrator Name |
| Booknumber | Varchar | None | 10 | Password |
| Borrowdate | Date | None | 10 | Borrowing time |
| Returndate | Date | None | 10 | Book return time |
| Remark | Varchar | None | 10 | Record remark information |

 

### **Chapter 3: Summary**

CURD of this library project is fully implemented, and the front-end uses fetch to request the REST-API service interface, perform additions, deletions, modifications, and queries, and connects to GCP-Mysql for data storage.


## Contribute

Contributions of any kind are welcome. Please ensure that your code follows this project's design and coding guidelines.

## License

This project uses the Apache 2.0 license. See the `LICENSE` file for more information.