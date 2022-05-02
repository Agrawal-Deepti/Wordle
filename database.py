import sqlite3
from logger import Logger


class Database(object):
    def __init__(self) -> None:
        self.logger = Logger('Database')
        try:
            self.con = sqlite3.connect('wordle.db')
            cur = self.con.cursor()
            # Create table
            cur.execute('''CREATE TABLE IF NOT EXISTS game 
                               (game_id integer NOT NULL PRIMARY KEY autoincrement,
                                played_date_time DATETIME DEFAULT CURRENT_TIMESTAMP, 
                                ip text NOT NULL, 
                                hidden_word text NOT NULL 
                                )''')

            cur.execute('''CREATE TABLE IF NOT EXISTS game_details 
                                       (game_id integer NOT NULL ,
                                        game_detail_id integer NOT NULL PRIMARY KEY autoincrement,
                                        trial_number integer NOT NULL,
                                        user_word text NOT NULL,
                                        matched_hidden_word text NOT NULL,
                                        played_date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                                        hints text,
                                        FOREIGN KEY(game_id) REFERENCES game(game_id)
                                        )''')
        except sqlite3.Error as e:
            self.logger.log(f"An error occurred while creating tables: {e.args[0]}")
        finally:
            self.con.commit()

    def logGameInDatabase(self, ip, hidden_word) -> int:
        try:
            cur = self.con.cursor()
            cur.execute("insert into game(ip, hidden_word) values (:ip,:hidden_word)",
                             {"ip": ip, "hidden_word": hidden_word})
        except sqlite3.Error as e:
            self.logger.log(f"An error occurred while inserting game: {e.args[0]}")
        finally:
            self.con.commit()
        return cur.lastrowid

    def logGameDetailsInDatabase(self, game_id: int, trial_number: int, user_word: str,
                                 matched_hidden_word: str, hints) -> None:
        try:
            cur = self.con.cursor()
            cur.execute("insert into game_details(game_id,trial_number,user_word, matched_hidden_word, hints) "
                             "values (:game_id, :trial_number, :user_word, :matched_hidden_word, :hints)",
                             {"game_id": game_id,
                              "trial_number": trial_number,
                              "user_word": user_word,
                              "matched_hidden_word": matched_hidden_word,
                              "hints": hints})
        except sqlite3.Error as e:
            self.logger.log(f"An error occurred while inserting game details: {e.args[0]}")
        finally:
            self.con.commit()

    def __str__(self) -> str:
        return f"Database initialized"



