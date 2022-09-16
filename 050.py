import sqlite3

conn = sqlite3.connect("mydatabase.db")
curs = conn.cursor()

# добавление персоналий (ID:autoincrement 1,2,3,4,5,6)
curs.execute("INSERT INTO PERSONS (full_name,degree,s_direction,workplace,department,post,country,sity,adress,work_phone,email) VALUES"
             "('Стрельцов Петр Никодимович','кандидат наук','химия','НИОПИК','технологии синтеза','доцент','Россия','Москва','ул.Б.Садовая, д.1','+7-495-181-11-88','niopik@mail.ru'),"
             "('Василенко Елена Дмитриевна','кандидат наук','ботаника','Институт ботаники им.Н.Г.Холодного','ботанические виды','руководитель','Украина','Киев','ул.Терещенковская, 2','+380-44-818895','evasil@mail.ua'),"             
             "('Новиков Дмитрий Исакович','доктор наук','химия','НИИХ','технологии полимеров','руководитель','Россия','Н.Новгород','пр.Гагарина, д.23,','+7-831-552-11-88','novik@mail.ru'),"
             "('Гаврушев Михаил Семенович','доктор наук','химия','НИИХ','технологии синтеза','зам.руководителя','Россия','Н.Новгород','ул.Пионерская, д.5,','+7-831-333-12-73','gavr@mail.ru'),"
             "('Савченко Лилия Петровна','ст.научн.сотрудник','генетика','Институт генетики НАН Беларуси','ДНК','зав.лабораторией','Беларусь','Минск','пр.Независимости, 66,','+375-17-58-52-25','igrb@mail.ru'),"
             "('Ринг Олег Владимирович','-','IT','Overone','Python','студент','Беларусь','Могилев','ул.Чигринова, 5/113','+375-29-350-73-45','workinplus@yandex.ru');")

# добавление конференций (ID:autoincrement 1,2,3,4,5,6)
curs.execute("INSERT INTO CONFERENCES (date_conf,place_conf,organizers,sponsors,num_of_days,num_of_participants,num_of_speakers) VALUES"
             "('2022-07-15','г.Минск','Петров И.Л., Сидоров А.И.','Иванов Д.В., Козлов Е.К.',2,4,3),"
             "('2022-08-12','г.Н.Новгород','Казаков Л.В., Сидоров А.И.','Яшин О.Д., Козлов Е.К.',1,3,3),"
             "('2022-08-20','г.Минск','Лисов С.П.','Яшин О.Д., Иванов Д.В., Козлов Е.К.',2,3,1),"
             "('2022-09-15','г.Могилев','Андреев Д.Л., Кот П.П.','Шершнев Ф.А., Никонов И.С.',1,3,1),"
             "('2022-09-30','г.Москва','Ефремова Л.С','Савченко С.С.',2,3,3);")

# добавление участников (ID:autoincrement 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
# последние три участника с пустыми датами: они еще не получили приглашение и не приехали, т.к. по состоянию на 16.09.2022 событие еще не наступило
curs.execute("INSERT INTO PARTICIPANTS (ID_person,ID_conference,when_sent_inv,when_got_app,is_thesis_got,when_arrived,is_need_hotel,when_departured) VALUES"
             "(1,1,'2022-07-08','2022-07-10',True,'2022-07-15',True,'2022-07-18'),"
             "(2,1,'2022-07-08','2022-07-10',False,'2022-07-14',True,'2022-07-17'),"
             "(3,1,'2022-07-09','2022-07-11',True,'2022-07-15',True,'2022-07-18'),"
             "(6,1,'2022-07-11','2022-07-13',True,'2022-07-15',True,'2022-07-18'),"
             "(1,2,'2022-08-02','2022-08-06',True,'2022-08-11',True,'2022-08-15'),"
             "(3,2,'2022-08-01','2022-08-05',True,'2022-08-12',False,'2022-08-16'),"
             "(5,2,'2022-08-05','2022-08-09',True,'2022-08-12',True,'2022-08-15'),"
             "(1,3,'2022-08-15','2022-08-17',False,'2022-08-20',False,'2022-08-20'),"
             "(3,3,'2022-08-14','2022-08-17',True,'2022-08-20',False,'2022-08-20'),"
             "(4,3,'2022-08-16','2022-08-18',False,'2022-08-20',False,'2022-08-20'),"
             "(2,4,'2022-09-10','2022-09-12',True,'2022-09-15',False,'2022-09-15'),"
             "(3,4,'2022-09-08','2022-09-11',False,'2022-09-15',False,'2022-09-15'),"
             "(6,4,'2022-09-09','2022-09-11',False,'2022-09-15',False,'2022-09-15'),"
             "(1,5,'2022-09-16','',True,'',False,''),"
             "(4,5,'2022-09-15','',True,'',True,''),"             
             "(5,5,'2022-09-15','',True,'',True,'');")

conn.commit()
curs.close()
conn.close()
