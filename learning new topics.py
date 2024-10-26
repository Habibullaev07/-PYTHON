'''CОЗДАНИЕ БАЗА ДАННЫХ'''
# import sqlite3

# connect = sqlite3.connect('my_database.db')

# cursor = connect.cursor()


# cursor.execute('''
#     CREATE TABLE users (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
#     )
# ''')

# connect.commit()
# connect.close()

'''ДОБАВЛЕНИЕ НА БАЗУ ДАННЫХ'''

# import sqlite3

# conection = sqlite3.connect('my_database.db')

# cursor = conection.cursor()

# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Jamshid', 17))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('isakndar', 17))

# conection.commit()
# conection.close()

'''ЧТЕНИЕ ДАННЫХ ИЗ ТАБЛИЦ'''

# import sqlite3

# connect = sqlite3.connect('my_database.db')

# cursor = connect.cursor()

# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)
    
# connect.close()

'''ОБНОВЛЕНИЕ ДАННЫХ'''

# import sqlite3

# conncetion = sqlite3.connect('my_database.db')

# cursor = conncetion.cursor()

# cursor.execute("UPDATE users SET age = ? WHERE name = ?", (17, 'Bilol'))

# conncetion.commit()
# conncetion.close()

'''УДАЛЕНИЕ ДАННЫХ'''

# import sqlite3

# connect = sqlite3.connect('my_database.db')

# cursor = connect.cursor()

# cursor.execute("DELETE FROM users WHERE name = ?", ('isаknder',))

# connect.commit()
# connect.close()

