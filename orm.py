
import sqlite3


def create_table_query(table, cols):
    columns_str = ', '.join([f"{k} {v}" for k, v in cols.items()])
    command = f'''CREATE TABLE IF NOT EXISTS {table} ({columns_str});'''
    return command


def insert_into_table(table, data):
    keys = ', '.join(data.keys())
    vals = ', '.join(map(repr, data.values()))
    query = f"INSERT INTO {table} ({keys}) VALUES ({vals})"
    return query


conn = sqlite3.connect('Company.db')

table_name = "Person"
columns = {
    "ID": "INT PRIMARY KEY NOT NULL",
    "NAME": "TEXT NOT NULL",
    "AGE": "INT NOT NULL",
    "ADDRESS": "CHAR(50)",
    "SALARY": "REAL"
}

cmd = create_table_query(table_name, columns)

person = {"ID": 1, "NAME": 'Paul', "AGE": 32, "ADDRESS": 'California', "SALARY": 20000.00}

query1 = insert_into_table(table_name, person)
print(query1)

# conn.execute(cmd)
# conn.close()

print('done!')
