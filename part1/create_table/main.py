# Cоздание таблицы
#
# Дана схема таблицы пациентов ветеринарной клиники:
#
# Id — идентификатор карты
# AnimalType — вид животного
# Sex — пол животного
# Name — кличка
# DateOfBirth — дата рождения
# Age — возраст (полных лет)
# Weight — вес (килограммы + граммы)
#
#
# Создайте таблицу в БД на основе этой схемы
import sqlite3
import prettytable

con = sqlite3.connect("animals.db")
cur = con.cursor()
sqlite_query = ("""CREATE TABLE animals_color(
Id integer PRIMARY KEY AUTOINCREMENT,
Color1 integer FOREIGN KEY color(id) ON DELETE SET NULL ON UPDATE CASCADE,
Color2 integer FOREIGN KEY color(id) ON DELETE SET NULL ON UPDATE CASCADE) """)
# TODO составьте запрос на создание таблицы
cur.execute(sqlite_query)

# Не удаляйте код ниже, он используется
# для вывода заголовков созданной таблицы

# ("""CREATE TABLE animals_color(
# Id integer PRIMARY KEY AUTOINCREMENT,
# Color1 integer,
# Color2 integer,
# FOREIGN KEY (Color1) REFERENCES color(id) ON DELETE SET NULL ON UPDATE CASCADE,
# FOREIGN KEY (Color2) REFERENCES color(id) ON DELETE SET NULL ON UPDATE CASCADE)  """
# )

# def print_result(sqlite_query):
#     cur.execute(sqlite_query)
#     result_query = ('SELECT * from animals')
#     table = cur.execute(result_query)
#     mytable = prettytable.from_db_cursor(table)
#     mytable.max_width = 30
#     print(mytable)
#
#
# if __name__ == '__main__':
#     print_result(sqlite_query)
