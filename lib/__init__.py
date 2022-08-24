import sqlite3

CONN = sqlite3.connect('db/music.db') # this obj represents connection to db

CURSOR = CONN.cursor()  ## cursor needed to execure sql statements
