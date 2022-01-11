import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="magazine"
)
myCur = mydb.cursor()

# sql = "CREATE DATABASE magazine"
# myCur.execute(sql)

""" Создание таблиц """

sql = ''' CREATE TABLE users (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            login VARCHAR(30),
            pass VARCHAR(30)
            )'''
myCur.execute(sql)


sql = ''' CREATE TABLE items (
            item_id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(50),
            price DECIMAL(8,2),
            category VARCHAR(30)
            )'''
myCur.execute(sql)


sql = ''' CREATE TABLE orders(
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                item_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (item_id) REFERENCES items (item_id)
                )'''
myCur.execute(sql)

""" ДОбавление записей """

"""Пользователи"""

sql = "INSERT INTO users (login, pass) VALUES(%s, %s)"
users=[("john", "some_pass"), ("alex", "some_pass")]
myCur.executemany(sql, users)
mydb.commit()

"""Товары"""

sql = "INSERT INTO items (title, price, category) VALUES(%s, %s, %s)"
items = [
    ("Кружка Мужская", 300, "cups"),
    ("Кепка красная", 150, "hats"),
    ("Кепка синяя", 200, "hats"),
    ("Кружка Женская", 400, "cups"),
    ("Красная Футболка", 550, "shirts"),
    ("Футболка 'Рик и Морти'", 700, "shirts"),
    ]
myCur.executemany(sql, items)
mydb.commit()

"""Заказы"""

sql = "INSERT INTO orders (user_id, item_id) VALUES(%s, %s)"
for i in range(1, 7):
    myCur.execute(sql, (random.randint(1, 2), i))
mydb.commit()

""" Запрос на вывод информации"""

sql = '''SELECT login, title
         FROM
             users
             INNER JOIN orders ON users.user_id = orders.user_id
             INNER JOIN items ON items.item_id = orders.item_id
 '''
myCur.execute(sql)
print("Все заказы:")
for el in myCur:
    print(f"{el[0]}  -  {el[1]}")





# sql = "DROP DATABASE magazine"
# myCur.execute(sql)