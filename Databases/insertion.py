import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')


cur.execute("INSERT INTO Tracks (title, plays) VALUES (?,?)",('One', 12))
cur.execute("INSERT INTO Tracks (title, plays) VALUES (?,?)",('Roots', 21))
#conn.commit()


print("Tracks:")
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
print("deleting rows which have plays more than 20")
cur.execute('DELETE FROM Tracks WHERE plays > 20')
#conn.commit()
print("after deletion")
cur.execute('SELECT title, plays FROM Tracks')
for row, k in cur:
    print(row, k)
conn.close()
