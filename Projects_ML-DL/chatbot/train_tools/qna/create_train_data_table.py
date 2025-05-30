import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
print(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
import pymysql
from config.DatabaseConfig import *

db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    sql = '''
        CREATE TABLE IF NOT EXISTS chatbot_train_data (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        intent VARCHAR(45) NULL,
        ner VARCHAR(1024) NULL,
        query TEXT NULL,
        answer TEXT NOT NULL,
        answer_image VARCHAR(2048) NULL,
        PRIMARY KEY (id)
        )'''

    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()