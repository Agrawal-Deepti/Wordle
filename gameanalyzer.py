import sqlite3
from sqlite3 import Date
from typing import IO
from logger import Logger


class GameAnalyzer(object):
    def __init__(self) -> None:
        self.logger = Logger('GameAnalyzer')
        self.con = sqlite3.connect('wordle.db')

    def generate_report(self, file_name: str, from_date, to_date) -> None:
        try:
            cur = self.con.cursor()
            games = cur.execute("select g.game_id, g.ip, g.hidden_word, g.played_date_time as game_date_time,"
                                "gd.game_detail_id, gd.trial_number, gd.user_word, gd.matched_hidden_word,"
                                "gd.hints, gd.played_date_time as trial_date_time"
                                " from game g, game_details gd where g.game_id = gd.game_id"
                                " and g.played_date_time >= :fromDate"
                                " and g.played_date_time <= :toDate  "
                                " order by g.game_id, gd.game_detail_id",
                                {"fromDate": from_date, "toDate": to_date})

            try:
                game_report_file: IO = open(file_name, 'w')
            except FileNotFoundError:
                self.logger.log(f"Can't open file {file_name}")
            else:
                for row in games:
                    game_report_file.write(f'{row}\n')
            finally:
                game_report_file.close()
        except sqlite3.Error as e:
            self.logger.log(f"An error occurred while fetching data from tables: {e.args[0]}")
        finally:
            self.con.close()


'''
To generate report  - Make sur eto change dates as per your need.
'''
gameAnalyzer = GameAnalyzer()
gameAnalyzer.generate_report("game_report.dat", '2022-05-02 00:00:00', '2022-05-02 23:59:59')
