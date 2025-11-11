import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
TABLE_NAME = 'customers'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(' 
    'id INTEGER PRIMARY KEY AUTOINCREMENT,' 
    'name TEXT,' 
    'weight REAL' 
    ')'
)

#WARNING: nesse comando sem o WHERE excluirá todos os dados da tabela
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

#sql = (
#     f'INSERT INTO {TABLE_NAME}'
#    '(name, weight)' \
#    'VALUES ' \
#    '(?, ?)' 
#)

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

cursor.execute(sql, ['Laura', 65])
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
))

connection.commit()

# Sql Injection, recomendado apenas se o usuário não insere dados a tabela.
#cursor.execute(
#    f'INSERT INTO {TABLE_NAME}'
#    '(id, name, weight)' \
#    'VALUES ' \
#    '(NULL, "Mariana", 56), (NULL, "Gabriela", 55), (NULL, "João", 75)' 
#)
#connection.commit()

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)