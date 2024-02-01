# Import necessary modules
import os.path
import sqlite3

class Leaderboard():
    """
    Class for handling a leaderboard stored in an SQLite database.

    Attributes:
    - db (sqlite3.Connection): SQLite database connection.
    """
    def __init__(self):
        """
        Initialize the Leaderboard class, creating the database if it does not exist.

        Parameters:
        None
        """
        if not os.path.exists("./leaderboards.db"):
            # Create database and Leaderboard table if not exists
            conn = sqlite3.connect("./leaderboards.db")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Leaderboard
                              (Racer TEXT, TopSpeed REAL)''')
            conn.commit()
            conn.close()

        self.db = sqlite3.connect(database="./leaderboards.db")

    def update_or_insert_score(self, racer, new_speed):
        """
        Update or insert a racer's top speed into the Leaderboard.

        Parameters:
        - racer (str): Racer's name.
        - new_speed (float): Racer's new top speed.

        Returns:
        None
        """
        conn = sqlite3.connect("leaderboards.db")
        cursor = conn.cursor()

        # Check if racer already exists
        cursor.execute("SELECT * FROM Leaderboard WHERE Racer=?", (racer,))
        existing_data = cursor.fetchone()

        if existing_data:
            if new_speed > existing_data[1]:  # 'TopSpeed' is at index 1
                cursor.execute("UPDATE Leaderboard SET TopSpeed=? WHERE Racer=?", (new_speed, racer))
                conn.commit()
        else:
            # Racer doesn't exist, insert new score
            cursor.execute("INSERT INTO Leaderboard (Racer, TopSpeed) VALUES (?, ?)", (racer, new_speed))
            conn.commit()

        conn.close()

    def retrieve_leaderboard_mph(self):
        """
        Retrieve the leaderboard sorted by top speed in descending order.

        Returns:
        - list: List of tuples containing racer and top speed.
        """
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Leaderboard ORDER BY TopSpeed DESC")
        rows = cursor.fetchall()
        return rows
