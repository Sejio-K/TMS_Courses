'''Задача 1: написать декоратор, который возвращает int вместо
float (хотим получить 1 вместо 1.5 как в примере)'''

def into_int(func):
    def wrapper(a, b):
        result = func(a, b)
        return int(result)
    return wrapper
@into_int
def div(a, b):
    return a / b

print(div(9,2))


'''Задача 2: написать декоратор, который позволяет сделать не более 3
 вызовов функции в секунду'''
import time
def start(f):
    last_time = None
    calls_in_last_second = 0
    def wrapper(*args, **kwargs):

