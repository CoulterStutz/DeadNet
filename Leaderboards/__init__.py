import os.path
import sqlite3

class Leaderboard():
    def __init__(self):
        if not os.path.exists("./leaderboards.db"):
            conn = sqlite3.connect("./leaderboards.db")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Leaderboard
                              (Racer TEXT, TopSpeed REAL)''')
            conn.commit()
            conn.close()

        self.db = sqlite3.connect(database="./leaderboards.db")


    def retrieve_leaderboard_mph(self):
        None