import sqlite3
class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect('Space_bot.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def check_human(self, id):
        self.cursor.execute(f'SELECT chatid FROM user_id WHERE chatid = "{id}"')
        return self.cursor.fetchone()
    
    def all_human(self, id):
        self.cursor.execute(f'SELECT username, name, surname FROM user_id WHERE chatid={id}')
        return self.cursor.fetchone()

    def new_human(self, id, list_names_surnames):
        self.cursor.execute('INSERT INTO user_id VALUES (?, ?, ?, ?, ?, ?, ?);', [id, list_names_surnames[0], 0, list_names_surnames[1], list_names_surnames[2], 0, 0])
        self.conn.commit()
    
    def score(self, id, number):
        self.cursor.execute(f'UPDATE user_id SET correct_otvet=correct_otvet+1 WHERE chatid={id}')
        self.cursor.execute(f'UPDATE user_id SET {number} WHERE chatid={id}')
        self.conn.commit()

    def delete_correct(self, id):
        self.cursor.execute(f'UPDATE user_id SET correct_otvet=correct_otvet*0 WHERE chatid={id}')
        self.conn.commit()

    def check_profile(self, id):
        self.cursor.execute(f'SELECT score, visit, correct_otvet FROM user_id WHERE chatid = {id}')
        return self.cursor.fetchone()

    def start_viktorina(self, id, random_number):
        current_question = {}
        self.cursor.execute(f'SELECT * FROM Викторина WHERE number = "{random_number}"')
        question = self.cursor.fetchone()
        current_question[id] = {
        'question': question[1],
        'otvet': question[5]
        }
        return [current_question, question]
        
    def visit(self, id):
        self.cursor.execute(f'UPDATE user_id SET visit = visit+1 WHERE chatid={id}')
        self.conn.commit()

    def start_section(self, choice, variant):
        name = choice[1:]
        self.cursor.execute(f'SELECT * FROM {name} WHERE name = "{variant}"')
        return self.cursor.fetchone()

    def start_predict(self, random_number):
        self.cursor.execute(f'SELECT * FROM Угадайка WHERE number = "{random_number}"')
        return self.cursor.fetchone()

