import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
creat_query = 'CREATE TABLE users (id int, username text,password text)'
cursor.execute(creat_query)
user = (1,"Bob","abcd")
insert_query = "INSERT INTO users values(?,?,?)"
cursor.execute(insert_query,user)
users = [
    (2,"rofl","xyz"),
    (3,"abc","zzz")
]
insert_many  = "insert into users values(?,?,?)"
cursor.executemany(insert_many,users)

connection.commit()
select_query = "select * from users"
for row in connection.execute(select_query) :
    print(row)
connection.close()
