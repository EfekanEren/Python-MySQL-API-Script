from xml.sax.handler import feature_external_ges
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="benutzername",
    password="passwort",
    database="dbname"
)

my_cursor = my_db.cursor()

sql = """
        INSERT INTO tabellenname (Datum, Hoechsttemperatur, Tiefsttemperatur, Feuchtigkeit) VALUE (
            '2022-08-26',
            '34',
            '22',
            '34'
        )
      """
      
my_cursor.execute(sql)
my_db.commit()


def show_all_data():
    my_cursor.execute("SELECT * FROM tabellenname")
    result = my_cursor.fetchall()

    for _ in result:
        print(_)


show_all_data


my_cursor.execute("SHOW DATABASES")