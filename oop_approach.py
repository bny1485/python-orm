import sqlite3


class DB:
    connection = None

    def __init_subclass__(cls, **kwargs):
        if cls.connection is None:
            cls.connection = sqlite3.connect('./database.sqlite')
        cmd = cls.create_table_query()
        cls.execute(cmd)

    def __init__(self, **kwargs):

        for k in self.get_columns():
            self.__setattr__(k, kwargs.get(k))

    @classmethod
    def execute(cls, cmd):
        return cls.connection.execute(cmd)

    @classmethod
    def get_columns(cls):
        return [k for k, v in cls.__dict__.items() if type(v) == str and not k.startswith('__')]

    @classmethod
    def create_table_query(cls):
        keys = cls.get_columns()
        columns_str = ', '.join([f"{k} {cls.__dict__[k]}" for k in keys])
        command = f'''CREATE TABLE IF NOT EXISTS {cls.__name__} ({columns_str});'''
        return command

    def insert_query(self):
        table = self.__class__.__name__
        data = self.__dict__
        keys = ', '.join(data.keys())
        vals = ', '.join(map(repr, data.values()))
        query = f"INSERT INTO {table} ({keys}) VALUES ({vals})"
        return query


class Person(DB):

    id = "INT PRIMARY KEY NOT NULL"
    name = "TEXT NOT NULL"
    age = "INT NOT NULL"
    address = "CHAR(50)"
    salary = "REAL"


class Whatever(DB):
    id = 'INT PRIMARY KEY NOT NULL'
    name = 'TEXT NOT NULL'
    last_name = 'TEXT'


print('-'*20)
print(Person.create_table_query())
person = Person(id=1, name='Paul', age=32, address='California', salary=20000.00)
print(person.insert_query())

print('-'*30)
print(Person.create_table_query())
print('-'*20)
print(Whatever.create_table_query())
