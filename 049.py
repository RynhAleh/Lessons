import sqlite3

conn = sqlite3.connect("mydatabase.db")
curs = conn.cursor()

# создание таблицы персоналий с уник.первичным ключом ID;
# создание таблицы конференций с уник.первичным ключом ID;
# создание таблицы участия с уник.первичным ключом ID, а также: ID персоны (кто будет), ID конференции (в какой будет)
curs.execute("""CREATE TABLE PERSONS (
       ID                   INTEGER PRIMARY KEY AUTOINCREMENT,
       full_name            TEXT (50),
       degree               TEXT (30),
       s_dirertion          TEXT (30),
       workplace            TEXT (50),
       department           TEXT (30),
       post                 TEXT (30),
       country              TEXT (30),
       sity                 TEXT (20),
       adress               TEXT (90),
       work_phone           TEXT (20),
       email                TEXT (30));""")
curs.execute("""CREATE TABLE CONFERENCES (
       ID                   INTEGER PRIMARY KEY AUTOINCREMENT,
       date_conf            DATE,
       place_conf           TEXT (20),
       organizers           TEXT,
       sponsors             TEXT,
       num_of_days          INTEGER,
       num_of_participants  INTEGER,
       num_of_speakers      INTEGER);""")
curs.execute("""CREATE TABLE PARTICIPANTS (
       ID                   INTEGER PRIMARY KEY AUTOINCREMENT,
       ID_person            INTEGER REFERENCES PERSONS (ID) ON DELETE CASCADE ON UPDATE CASCADE,
       ID_conference        INTEGER REFERENCES CONFERENCES (ID) ON DELETE CASCADE ON UPDATE CASCADE,
       when_sent_inv        DATE,
       when_got_app         DATE,
       is_thesis_got        BOOLEAN,
       when_arrived         DATE,
       is_need_hotel        BOOLEAN,
       when_departured      DATE);""")
conn.commit()
curs.close()
conn.close()
