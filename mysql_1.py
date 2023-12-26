import mysql.connector

class MySQL():
    def __init__(self) -> None:
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()


    def ConnectDB(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user='root',
            password='18011996'
        )
        self.cursor = self.db.cursor()
    
    def CreateDB(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS foundation;')
        self.cursor.execute('USE foundation;')
    
    def CreateTB(self):
        self.cursor.execute("DROP TABLE IF EXISTS Registry;")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Registry(
                            id INT,
                            login TEXT,
                            password TEXT,
                            first_name TEXT,
                            email TEXT,
                            position TEXT
                            );""")
        
    def InsertTB(self):
        with open('new.sql') as f:
            for i in f.read().split('\n'):
                if "Senior" in i:
                    self.cursor.execute(i)
        self.db.commit()

    def FirstQuery(self):
        self.cursor.execute("SELECT * FROM registry WHERE position LIKE '%senior%';")
        # print(self.cursor.fetchall())
        for i in self.cursor.fetchall():
            print(i)

        # print(len(self.cursor.fetchall()))
        

mysql = MySQL()
mysql.InsertTB()
mysql.FirstQuery()