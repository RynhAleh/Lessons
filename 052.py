import sqlite3

conn = sqlite3.connect("mydatabase.db")
curs = conn.cursor()

print("Удаление приглашений, отправленных после второй половины августа ...")
curs.execute("DELETE FROM PARTICIPANTS WHERE when_sent_inv >= '2022-08-15';")
print("Удаление августовских конференций ...")
curs.execute("DELETE FROM CONFERENCES  WHERE date_conf BETWEEN '2022-08-01' AND '2022-08-31';")
print("Удаление персоналий-химиков ...")
curs.execute("DELETE FROM PERSONS WHERE s_direction = 'химия';")
print("Изменение персоналий (телефон -> пустой) ...")
curs.execute("UPDATE PERSONS SET work_phone = '';")
print("Изменение мест проведения конференций (Минск -> Москва) ...")
curs.execute("UPDATE CONFERENCES SET place_conf = 'г.Москва' WHERE place_conf = 'г.Минск';")
print("Изменение приглашений (дата выбытия -> пустая) ...")
curs.execute("UPDATE PARTICIPANTS SET when_departured = ''")
conn.commit()

print("\n----------ЧТО ОСТАЛОСЬ С ПЕРСОНАЛИЙ-------------")
curs.execute("SELECT * FROM PERSONS;")
print(*curs.fetchall(), sep="\n")
print("\n----------ЧТО ОСТАЛОСЬ С КОНФЕРЕНЦИЙ-------------")
curs.execute("SELECT * FROM CONFERENCES;")
print(*curs.fetchall(), sep="\n")
print("\n----------ЧТО ОСТАЛОСЬ С ПРИГЛАШЕНИЙ К УЧАСТИЮ-------------")
curs.execute("SELECT * FROM PARTICIPANTS;")
print(*curs.fetchall(), sep="\n")

curs.close()
conn.close()
