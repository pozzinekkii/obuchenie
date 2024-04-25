from peewee import *


db = PostgresqlDatabase('dz',
                        user='postgres',
                        password='root',
                        host='localhost',
                        port=5432)


class Author(Model):
    name = CharField()

    class Meta:
        database = db


class Book(Model):
    title = CharField()
    author = ForeignKeyField(Author, backref='book')

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Author, Book])



