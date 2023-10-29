
import sqlite3 as sl
import os

class ParseToDB():
    def __init__(self) -> None:
        self.data = self.parse()
    
    "парсит бд"
    def parse(self):
        with open('xlsx/knowledge_base.txt', 'r') as f:
            f = f.readlines()
            f.pop(0)
        ret = []
        for i in f:
            ret.append(i.split('\t'))
        [i.pop(0) for i in ret]
        return ret
        
    def insert_db(self):
        try:
            con = sl.connect('knowledge_base.db')
            cur =  con.cursor()
            """
            ДОБАВЛЕНИЕ ДАННЫХ ИЗ БАЗЫ ЗНАНИЙ
            """
            # for dt in self.data:
            #     cur.execute(
            #         """
            #         INSERT INTO knowledgeBase (type, name, number, date_exit, date_enter, key_word) VALUES (?, ?, ?, ?, ?, ?)
            #         """, dt)
            # con.commit()


            """
            ДОБАВЛЕНИЕ ФАЙЛОВ
            """
            files = os.listdir(path=r'D:\Ярлыки\IT\Project\hackaton\files')
            for file_path in files:
                file_info = str(os.stat(fr"D:\Ярлыки\IT\Project\hackaton\files\{file_path}").st_size) + ' байт'
                cur.execute(
                    F"""
                    UPDATE knowledgeBase SET file_path = ?, file_info = ? WHERE name = ?
                    """, (fr"D:\Ярлыки\IT\Project\hackaton\files\{file_path}", file_info, str(file_path)[:-4])
                )
                
            con.commit()
            return 'inserted in db'
        except sl.Error as ex:
            return(ex)
        finally:
            cur.close()
            con.close()


a = ParseToDB()
# print(a.data[0][-1])
print(a.insert_db())
# print(a.data)