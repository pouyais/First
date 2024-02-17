import sqlite3


class  database():
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS student(fname text,lanme text,score integer )")
        self.con.commit()



    def insertt(self,fname,lname,score):
        self.cur.execute("""INSERT INTO student VALUES (?,?,?)""", (fname,lname,score))
        self.con.commit()


