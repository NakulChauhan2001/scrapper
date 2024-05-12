import mysql.connector
def db():
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="qwerty12345",
    database="scrapper_db"
    )
    return dataBase