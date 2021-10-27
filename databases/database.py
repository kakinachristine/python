from peewee import*
from os import path
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Myschool.db"))
class Users(Model):
    name = CharField()
    email = CharField()
    password = CharField()
    age = IntegerField
    class Meta:
        database = db
Users.create_table(fail_silently=True)
Users.create(name = "mjomba",email="mjomba@gmail.com",password = "mjomba123", age=100)
users = Users.select()
for person in users:
    print(person.name, person.email, person.age, person.password)