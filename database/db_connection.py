import mysql.connector
from logs.loger_config import logger

class ConnectDb:

    def __init__(self):
        self.config = { 
                "host": "localhost",
                "user": "root",
                "password": "secret",
                "database": "librarydb"}
        self._connect = None
        self.cursor = None

    def connect(self):
        if self._connect:
            return self._connect
        try:
            self._connect = mysql.connector.connect(**self.config)
            return self._connect        
        except Exception as e:
            print(e)

    def create_book_table(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""CREATE TABLE if not exists books(id INT AUTO_INCREMENT PRIMARY KEY
                    ,title VARCHAR(50) not NULL,
                    author VARCHAR(50) not NULL,
                    genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other') NOT NULL,
                    is_available BOOLEAN DEFAULT True,
                    id_member_by_borrowed int DEFAULT null
                    )""")
        db.commit()

    def create_member_table(self):
        db = self.connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""CREATE TABLE if not exists members(id INT not null
                    ,name VARCHAR(50) not NULL,
                    email VARCHAR(50) unique not NULL,
                    is_active BOOLEAN DEFAULT True,
                    borrows_total INT AUTO_INCREMENT PRIMARY KEY
                    )""")
        db.commit()

