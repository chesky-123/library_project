from database.db_connection import ConnectDb
from logs.loger_config import logger
from models import book_model



class BookDB:

    def __init__(self):
        self.db = ConnectDb()
        self.connection = self.db.connect()
        self.cursor = self.connection.cursor(dictionary=True)


    def create_new_book(self,body):
        self.cursor.execute(""" 
                    insert INTO books(title ,author ,genre) 
                    VALUES(%s,%s,%s)
                    """,(body["title"] ,body["author"] ,body["genre"]))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def get_book_by_id(self,id):
        self.cursor.execute("select * from books WHERE id = %s",(id,))
        return self.cursor.fetchall()

    def update_book(self, id, data):
        self.cursor.execute("""update books set title = %s ,
                            author = %s ,
                            genre = %s 
                            where id = %s
                            """,(data["title"],data["author"],data["genre"] ,id))
        self.connection.commit()
        return self.cursor.rowcount > 0
    


    def set_available(self, id, val,member_id):
        self.cursor.execute("""update books 
                            set is_available = %s,
                            id_member_by_borrowed = %s
                            where id = %s
                            """,(val ,member_id ,id))    
        self.connection.commit()
        return self.cursor.rowcount > 0

    def count_total_books(self):
        self.cursor.execute("select count(*) from books")
        return self.cursor.fetchall()

    def count_return_books(self):
        self.cursor.execute("select count(*) from books where is_available=%s",(True,))
        return self.cursor.fetchall()

    def count_borrowed_books(self):
        self.cursor.execute("select count(*) from books where is_available=%s",(False,))
        return self.cursor.fetchall()

    def count_by_genre(self,genre):
        self.cursor.execute("SELECT count(*) FROM books GROUP BY %s",(genre,))
        return self.cursor.fetchall()

    def count_active_borrows_by_member(self,member_id):
        self.cursor.execute("SELECT COUNT(*) FROM books WHERE id_member_by_borrowed = %s",(member_id,))
        return self.cursor.fetchall()


