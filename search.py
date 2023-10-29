import sqlite3 as sl


class Search():
    def __init__(self) -> None:
        self.way_search = None
        self.tag = None
        self.answer = None

    def get_user(self, id):
        con = sl.connect('knowledge_base.db')
        cur = con.cursor()
        cur.execute("SELECT * from users")
        self.tag = cur.fetchone()[0]
        return cur.fetchall()

    def get_data(self, id):
        con = sl.connect('knowledge_base.db')
        cur = con.cursor()
        cur.execute("SELECT * from knowledgeBase WHERE id = ?", (id, ))
        ret = cur.fetchall()[0]
        return f"Тип: {ret[1]}\nИмя: {ret[2]}\nНомер: {ret[3]}\nДата выхода: {ret[4]}\nДата ввода в действие: {ret[5]}\nОбъем: {ret[8]}"
    
    def search(self, inpt, tag):
        con = sl.connect('knowledge_base.db')
        cur = con.cursor()
        inpt = str(inpt)
        match self.way_search:
            case 'keyword':
                cur.execute(
                    """
                    SELECT key_word, name, tag FROM knowledgeBase
                    """
                )
                data = cur.fetchall()
                self.answer = '\n'.join([dt[1] for dt in data if (dt[2] == tag or dt[2] == 'все') and inpt.lower() in dt[0].lower()])
                # return ''.join([dt[1] for dt in data if (dt[2] == tag or dt[2] == 'все') and inpt.lower() in dt[0].lower()])
            case 'type':
                cur.execute(
                    """
                    SELECT type, name, tag FROM knowledgeBase
                    """
                )
                data = cur.fetchall()
                self.answer = [dt[1] for dt in data if (dt[2] == tag or dt[2] == 'все') and inpt.lower() in dt[0].lower()]
           
            case 'name':
                cur.execute(
                    """
                    SELECT name, tag FROM knowledgeBase
                    """ 
                )
                data = cur.fetchall()
                self.answer = [dt[0] for dt in data if (dt[1] == tag or dt[1] == 'все') and inpt.lower() in dt[0].lower()]
            
            case 'number':
                cur.execute(
                    """
                    SELECT number, name, tag FROM knowledgeBase
                    """
                )
                data = cur.fetchall()
                self.answer = [dt[1] for dt in data if (dt[2] == tag or dt[2] == 'все') and inpt.lower() in str(dt[0]).lower()]
            
            case 'date_exit':
                cur.execute(
                    """
                    SELECT date_exit, name, tag FROM knowledgeBase
                    """
                )
                data = cur.fetchall()
                self.answer = [dt[1] for dt in data if (dt[2] == tag or dt[2] == 'все') and inpt.lower() in str(dt[0]).lower()]
            
            case 'date_enter':
                cur.execute(
                    """
                    SELECT date_enter, name, tag FROM knowledgeBase
                    """
                )
                data = cur.fetchall()
                self.answer = [dt[1] for dt in data if (dt[2] == tag or dt[2] == 'все') and inpt.lower() in str(dt[0]).lower()]


a = Search()
a.way_search = 'keyword' #тип поиска
a.search('технологии', 'инженер') #входные данные: "технологии" - ключевое слово, "инженер" - должность
print(a.answer)