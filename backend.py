import sqlite3

class Bookstore:

    def __init__(self):
        self.connect()
        self.cur.execute("CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY,title TEXT , author text ,year INTEGER , isbn INTEGER)")
        self.con.commit()


    def connect(self):
        self.con = sqlite3.connect("bookslist.db")
        self.cur = self.con.cursor()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO store VALUES (NULL,?,?,?,?)",(title,author,year ,isbn))
        self.con.commit()


    def view(self):
        self.connect()
        self.cur.execute("SELECT * FROM store")
        self.rows=self.cur.fetchall()
        return self.rows

    def delete(self,id):
        self.cur.execute("DELETE FROM store WHERE id=?",(id,))
        self.con.commit()


    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM store WHERE isbn= ? OR author= ? OR title = ? OR year = ?",(isbn,author,title,year))
        self.rows= self.cur.fetchall()
        return self.rows

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE store SET title =?, author=?,year=?,isbn=? WHERE id = ?",(title,author,year,isbn,id))
        self.con.commit()

    def __del__(self):
        self.con.close()

"""
def main():
    ob=Bookstore()
    ob.update(9,author="marvel")
    #ob.delete(7)
    for _ in ob.view():
        print(_)


if __name__=="__main__":
    main()
"""
