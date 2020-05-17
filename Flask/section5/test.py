import sqlite3

connection = sqlite3.connect('data.db')

# cursor allows you to select things and start things
# responsible for executing the queries
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

# To run the query
cursor.execute(create_table)

# inserting one value
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users Values (?,?,?)"
cursor.execute(insert_query, user)

# inserting many values
users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)

# to retrieve data
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


# whenever we insert the data we have to tell the connection to actually
# save all of our changes into the disk(data.db file)
connection.commit()

connection.close()
