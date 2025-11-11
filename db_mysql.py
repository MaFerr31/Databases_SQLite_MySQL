import pymysql  # type: ignore
import os
import dotenv # type: ignore

TABLE_NAME = 'customers'
dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)



with connection:
    with connection.cursor() as cursor:
        cursor.execute(
             f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (' \
            'id INT NOT NULL AUTO_INCREMENT, ' \
            'name VARCHAR(50) NOT NULL, ' \
            'idade INT NOT NULL, ' \
            'PRIMARY KEY (id)' \
            ')'
        )
        cursor.execute(f'TRUNCATE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) ' \
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data = {
            "name": "Gabriela",
            "age": 15
        }
        result = cursor.execute(sql, data)
        #print(sql, data)
        #print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) ' \
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data_many = (
            {"name": "Gabriela", "age": 14},
            {"name": "Bruno", "age": 21},
            {"name": "Mauro", "age": 63},

        )
        result = cursor.executemany(sql, data_many)
        #print(sql, data)
        #print(result)
    connection.commit()
#connection.close()