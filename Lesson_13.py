import requests
import json

class Todo:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

class Todos:
    def __init__(self):
        self.todos = []

    def fetch_data(self):
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        if response.status_code == 200:
            todo_data = response.json()
            self.todos = [Todo(data['id'], data['title'], data['completed']) for data in todo_data]

    def __iter__(self):
        return iter(self.todos)

    def get_todo_by_id(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def to_json(self):
        return json.dumps([todo.__dict__ for todo in self.todos])

    @classmethod
    def from_json(cls, json_data):
        todos = cls()
        todo_data = json.loads(json_data)
        todos.todos = [Todo(data['id'], data['title'], data['completed']) for data in todo_data]
        return todos

# Пример использования
todos = Todos()
todos.fetch_data()

# Итерация по объекту Todos
for todo in todos:
    print(f"ID: {todo.id}, Title: {todo.title}, Completed: {todo.completed}")

# Получение todo по ID
todo_1 = todos.get_todo_by_id(1)
if todo_1:
    print(f"Todo with ID 1: {todo_1.title}")
else:
    print("Todo with ID 1 not found")

# Сериализация и десериализация
json_data = todos.to_json()
print("Serialized data:")
print(json_data)

deserialized_todos = Todos.from_json(json_data)
for todo in deserialized_todos:
    print(f"Deserialized Todo: ID: {todo.id}, Title: {todo.title}, Completed: {todo.completed}")
