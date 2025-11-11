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
            {"name": "Rafaela", "age": 14},
            {"name": "Bruno", "age": 21},
            {"name": "Mauro", "age": 63},
            {"name": "Marcelo", "age": 21},
            {"name": "João", "age": 63},
            {"name": "Isadora", "age": 85},

        )
        result = cursor.executemany(sql, data_many)
        #print(sql, data)
        #print(result)
    connection.commit()

    #Lendo valores com SELECT
    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
             'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        print(cursor.mogrify(sql, (menor_id, maior_id)))
        data_select = cursor.fetchall()
        for row in data_select:
            print(row)

#connection.close()