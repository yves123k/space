


import sqlite3
def create_table():
        connexion=sqlite3.connect('DATA_USER.db')
        curseur=connexion.cursor()
        try:
            curseur.execute(""" SELECT * FROM data_users """)
        except:
            curseur.execute("""CREATE TABLE IF NOT EXISTS Users_contact(
                ADMIN_Account_id INTEGER NOT NULL PRIMARY KEY,
                Name text,
                Numero text,
                Photo text) """)
            curseur.execute("""CREATE TABLE IF NOT EXISTS USERS_Account(
                Name text,
                Email text,
                Password text) """)

            connexion.commit()
            connexion.close()