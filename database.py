import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="",
  host="127.0.0.1",
  port="5432"
)

#создание таблицы
cur = con.cursor()
cur.execute('''CREATE TABLE USERS  
     (datetime TEXT NOT NULL,
     id TEXT NOT NULL,
     action TEXT NOT NULL,
     phone TEXT NOT NULL,
     duration TEXT NOT NULL,
     recognizing TEXT NOT NULL
     );''')

con.commit()
con.close()

def add_info(datetime, id, action, phone, duration, recognizing):
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO STUDENT (datetime, id, action, phone, duration, recognizing) VALUES ('{datetime}', '{id}', '{action, phone}', '{duration}', '{recognizing}')"
    )
    con.commit()
    con.close()
