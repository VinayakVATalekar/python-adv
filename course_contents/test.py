import sqlite3

connection=sqlite3.connect('data.db')

cursor=connection.cursor()

create_table="create table users (id int,username text,password text)"
cursor.execute(create_table)

user=(1,"jose","abcd")
insert_query="insert into users values(?,?,?) "
cursor.execute(insert_query,user)

users=[
    (2,'heyja',"abcd"),
     (3,'hey',"abcd")
 ]

cursor.executemany(insert_query,users)
select_query="select * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
