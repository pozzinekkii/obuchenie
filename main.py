from models import *

#методы для создания записей
# Employee.create(id=1, name='Nick', age=24, salary=10000)
# Employee.create(id=2, name='Tom', age=20, salary=18900)

#методы для чтения
# employee = Employee.select()
# for user in employee:
#     print(user.name, user.age, user.salary)

# employee = Employee.get(Employee.id == 1)
# print(employee.name, employee.age, employee.salary)

#метод для обновления записи
# employee = Employee.get(Employee.id == 2)
# employee.name = 'Tom'
# employee.save()
# Employee.update(age=30).where(Employee.id == 2).execute()

#метод для удаления записи
# user = Employee.get(Employee.id == 1)
# user.delete_instance()
# Employee.delete().where(Employee.id == 2).execute()

#фильтрация
# employee = Employee.select().where(Employee.name == 'Tom')
# for user in employee:
#     print(user.name, user.age, user.salary)


#and
# employee = Employee.select().where((Employee.name == 'Tom') & (Employee.age == 20))
# for user in employee:
#     print(user.name, user.age, user.salary)


#or
# employee = Employee.select().where((Employee.name == 'Tom') | (Employee.age == 20))
# for user in employee:
#     print(user.name, user.age, user.salary)

#like
# employee = Employee.select().where(Employee.name ** 'N%')
# for user in employee:
#     print(user.name, user.age, user.salary)


#in
# employee = Employee.select().where(Employee.age << [20,30])
# for user in employee:
#     print(user.name, user.age, user.salary)

#between
# employee = Employee.select().where(Employee.age.between(20,30))
# for user in employee:
#     print(user.name, user.age, user.salary)

# author1 = Author.create(name='Steven King')
# author2 = Author.create(name='J.K. Rowling')
#
# book1 = Book.create(title='The Shining', author=author1)
# book2 = Book.create(title='Harry Potter', author=author2)
# book3 = Book.create(title='Onegin')
# author3 = Author.create(name='A.S. Pushkin')

# query = (Book.select(Book.title, Author.name)
#          .join(Author).dicts())
# for row in query:
#     print(row)

# query = (Book.select(Author.name, Book.title)
#          .join(Author, JOIN.RIGHT_OUTER).dicts())
#
# for row in query:
#     print(row)

# query = (Book.select(Book.title, Author.name)
#          .join(Author, JOIN.LEFT_OUTER).dicts())
# for row in query:
#     print(row)

# query = (Book.select(Author.name, Book.title)
#          .join(Author, JOIN.FULL).dicts())
# for row in query:
#     print(row)

# query = (Book.select(Author.name, Book.title)
#          .join(Author, JOIN.CROSS).dicts())
# for row in query:
#     print(row)

query = Book.select(Book.title, Author.name).join(Author, JOIN.LEFT_OUTER)
for row in query:
    book = row
    author = book.author
    print(f'{book.title} - {author.name}')