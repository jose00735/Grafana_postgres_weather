import psycopg2

conn = psycopg2.connect(database="postgres",
                         host="localhost",
                         user="grafana",
                         password="grafana",
                         port="5432")

cursor = conn.cursor()

cursor.execute("CREATE TABLE clima (id int PRIMARY KEY, temp int, humidity int);")
cursor.execute("INSERT INTO clima (id,temp,humidity) VALUES (1,14, 74);")
conn.commit()
#cursor.execute("SELECT * FROM clima;")
#rows = cursor.fetchall()
#for row in rows:
#    print(row)
