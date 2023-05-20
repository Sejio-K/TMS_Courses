'''Напишите генератор, который будет генерировать числа от 0 до бесконечности и вызовите его несколько раз'''
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1


gen1 = infinite_numbers()


for i in range(5):
    print(next(gen1))



'''Напишите генератор, который будет генерировать числа от 0 до бесконечности и вызовите его несколько раз'''

class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.max_num:
            num = self.current_num
            self.current_num += 1
            return num
        else:
            raise StopIteration




max_num = int(input("Введите максимальное число: "))
my_iterator = MyIterator(max_num)


for num in my_iterator:
    print(num)


'''Допишите класс Family таким образом чтобы он влялся итератором и мы могли при помощи цикла for вывести всех ченов семьи
Допишите классы таким образом чтобы у FamilyMember был id и в классе Family мы могли найти member по id'''


class FamilyMember:
    member_id = 0  # статическая переменная, которая будет инкрементироваться при создании нового объекта

    def __init__(self, name, role=None, age=None):
        self.id = FamilyMember.member_id
        FamilyMember.member_id += 1
        self.name = name
        self.role = role
        self.age = age

    def __str__(self):
        return f"FamilyMember {self.id}: {self.name}, role: {self.role}"


class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def __len__(self):
        return len(self.members)

    def add_family_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"

    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        raise ValueError(f"Member with id {member_id} not found")


'''генератор чисел Фибоначчи'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))
