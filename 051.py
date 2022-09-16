import sqlite3

conn = sqlite3.connect("mydatabase.db")
curs = conn.cursor()

print("-----------ВСЕ ПЕРСОНАЛИИ:-------------")
curs.execute("SELECT * FROM PERSONS")
print(*curs.fetchall(), sep="\n")

print("\n-----------КОНФЕРЕНЦИИ С ИЮЛЯ ПО АВГУСТ 2022:-------------")
curs.execute("SELECT * FROM CONFERENCES WHERE date_conf BETWEEN '2022-07-01' AND '2022-08-31'")
print(*curs.fetchall(), sep="\n")

print("\n-----------ФИО ПРИГЛАШЕННЫХ НА ВЫШЕУКАЗАННЫЕ КОНФЕРЕНЦИИ (В АЛФАВИТНОМ ПОРЯДКЕ):-------------")
curs.execute("SELECT full_name FROM PERSONS WHERE ID IN("
             "SELECT ID_person FROM PARTICIPANTS WHERE ID_conference IN("
             "SELECT ID FROM CONFERENCES WHERE date_conf BETWEEN '2022-07-01' AND '2022-08-31'"
             ")) ORDER BY full_name")
print(*curs.fetchall(), sep="\n")

curs.close()
conn.close()
