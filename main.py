class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.tables = {}

    def create_table(self, table_name, columns):
        self.tables[table_name] = columns

    def insert(self, table_name, data):
        if table_name in self.tables:
            self.tables[table_name].append(data)
        else:
            raise Exception("Table not found")

    def select(self, table_name):
        if table_name in self.tables:
            return self.tables[table_name]
        else:
            raise Exception("Table not found")

    def update(self, table_name, data, condition):
        if table_name in self.tables:
            for i, row in enumerate(self.tables[table_name]):
                if condition(row):
                    self.tables[table_name][i] = data
        else:
            raise Exception("Table not found")

    def delete(self, table_name, condition):
        if table_name in self.tables:
            self.tables[table_name] = [row for row in self.tables[table_name] if not condition(row)]
        else:
            raise Exception("Table not found")


class Model:
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name

    def create(self, data):
        self.db.insert(self.table_name, data)

    def read(self):
        return self.db.select(self.table_name)

    def update(self, data, condition):
        self.db.update(self.table_name, data, condition)

    def delete(self, condition):
        self.db.delete(self.table_name, condition)


class Field:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class CharField(Field):
    def __init__(self, name, max_length):
        super().__init__(name, "char")
        self.max_length = max_length


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, "integer")


class User(Model):
    def __init__(self, db):
        super().__init__(db, "users")
        self.fields = [
            CharField("name", 255),
            IntegerField("age")
        ]


class Post(Model):
    def __init__(self, db):
        super().__init__(db, "posts")
        self.fields = [
            CharField("title", 255),
            CharField("content", 1000)
        ]


db = Database("my_database")
user = User(db)
post = Post(db)

db.create_table("users", [])
db.create_table("posts", [])

user.create({"name": "John", "age": 25})
post.create({"title": "Hello", "content": "World"})

print(user.read())
print(post.read())

user.update({"name": "Jane", "age": 30}, lambda x: x.get("name") == "John")
post.update({"title": "Hi", "content": "Universe"}, lambda x: x.get("title") == "Hello")

print(user.read())
print(post.read())

user.delete(lambda x: x.get("name") == "Jane")
post.delete(lambda x: x.get("title") == "Hi")

print(user.read())
print(post.read())