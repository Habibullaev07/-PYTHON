import sqlite3

with sqlite3.connect('my_basedate1.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                    )
                    ''')

    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('jamshidbek', 17))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('robot', 100))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('NOLAN', 12))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('layn', 10))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('masha', 16))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('franco', 13))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('frensis', 17))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('ruby', 1))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('laya', 22))
    # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('robot', 15))
    
    
    # cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
    #     ('jamshidbek', 17),
    #     ('robot', 100),
    #     ('NOLAN', 12),
    #     ('layn', 10),
    #     ('masha', 16),
    #     ('franco', 13),
    #     ('frensis', 17),
    #     ('ruby', 1),
    #     ('laya', 22),
    #     ('robot', 15)
    #     ])
        



    cursor.execute("UPDATE users SET name = 'fashal' WHERE id = 1")
    cursor.execute("UPDATE users SET name = 'lena' WHERE age = 100")


    # cursor.execute("DELETE FROM users ")

    cursor.execute("SELECT * FROM users")

    # result = cursor.fetchone()
    # print(result)

    result = cursor.fetchall()

    # result = cursor.fetchmany(7)
    for res in result:
        print(res)
