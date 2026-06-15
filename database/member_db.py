from database.db_connection import ConnectDb


class Member_db:
    def __init__(self):        
        self.db = ConnectDb()
        self.connection = self.db.connect()
        self.cursor = self.connection.cursor(dictionary=True)


    def create_member(self,data):
        self.cursor.execute("""
                            INSERT INTO members(name ,email ,is_active ,borrows_total)
                            VALUES(%s,%s,%s,0)
                            """
                            ,(data["name"] ,data["email"] ,True))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_all_members(self):
        self.cursor.execute("select * from members")
        return self.cursor.fetchall()
    
    def get_member_by_id(self,id):
        self.cursor.execute("select * from members where id = %s",(id,))
        return self.cursor.fetchall()

    def update_member(self ,id ,data):
        self.cursor.execute("""
                            update members 
                            set name = %s,
                            email = %s 
                            where id = %s
                            """,
                            (data["name"],data["email"],id))
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def deactivate_member(self ,id):
        self.cursor.execute("update members set is_active = %s where id = %s",(False,id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def activate_member(self ,id):
        self.cursor.execute("update members set is_active = %s where id = %s",(True,id))
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def increment_borrows(self ,id):
        self.cursor.execute("update members set borrows_total = borrows_total + 1 where id = %s",(id,))
        self.connection.commit()
        return self.cursor.rowcount > 0 
    
    def count_active_members(self):
        self.cursor.execute("select * from members where is_active = %s",(True,))
        return self.cursor.fetchall()

    def get_top_member(self):
        self.cursor.execute("SELECT * FROM members ORDER BY borrows_total DESC LIMIT 1")
        return self.cursor.fetchall()




