import sqlite3

dbconn = sqlite3.connect('market.db')

dbcursor = dbconn.cursor()
dbcursor.execute("create table if not exists market \
         (id_code integer primary key, \
             name text \
             amount integer, \
             unit_price integer, \
            total_price integer )")

dbcursor.close()
dbconn.close()
