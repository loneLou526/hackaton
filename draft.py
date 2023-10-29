import sqlite3 as sl
import os

con = sl.connect('knowledge_base.db')
cur = con.cursor()
a = ['инженер', 'инженер', 'юрист', 'юрист', 'управ. качеством', 'все', 'все', 'бухгалтер', 'инженер', 'все', 'юрист']

c = 1
# for i in a:
#     cur.execute(
#     """
#     UPDATE knowledgeBase SET tag = ? WHERE id = ?
#     """, (i, c))
#     c += 1
#     con.commit()
# cur.execute("""
#             INSERT INTO users (name, login, tag) VALUES(?, ?, ?)
#     """, ('Саша', '864496207'))
# cur.execute("DROP TABLE users")
con.commit() 
# cur.execute("""
#             CREATE TABLE knowledgeBase (
#                 id INTEGER PRIMARY KEY,
#                 type TEXT,
#                 name TEXT,
#                 number INTEGER,
#                 date_exit DATE,
#                 date_enter DATE,
#                 key_word TEXT,
#                 file_info TEXT,
#                 tag TEXT
#             )
#         """)
# cur.execute("""
#             CREATE TABLE users (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 login INTEGER,
#                 TAG TEXT    
#             )
# """)
# a = ['ГОСТ (гос. стандарт)', 'Информационные технологии. Комплекс стандартов на автоматизированные системы управления', '34.602- 2020', '22.12.2020', '01.01.2022', '\n']
# cur.execute(
#     """INSERT INTO knowledgeBase (type, name, number, date_exit, date_enter, key_word) VALUES (?, ?, ?, ?, ?, ?)
#     """, (a))
con.commit()

# files = os.listdir(path=r'D:\Ярлыки\IT\Project\hackaton\files')
# print(files)