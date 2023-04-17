
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_ab = [elem_a for elem_a in a if elem_a in b]
print(common_ab )



#Задание 2: написать программу для вычисления факториала. Факториал - 1 * 2 * 3 ... * n

number = int(input('Введите число: '))
faktorial_n = 1
for k in range(1, number + 1):
    faktorial_n *= k
print('Факториал числа', number, '=', faktorial_n)



'''Задание 3: объявить функцию, которая принимает в себя любое 
количество словарей и возвращает единый словарь, в котором есть
ключи из всех переданных словарей'''

dictionary_data = {}
def dictionary(input_data):
    dictionary_data.update(input_data)
    print(dictionary_data)
    return dictionary_data

a = {'марафон': 'гонка бегунов длиной около 26 миль',
'персона': 'человек',
'бежал': 'бежать в прошедшем времени'}
dictionary(a)

b = {'бежать': 'двигаться со скоростью',
'туфля': 'род обуви, закрывающей ногу не выше щиколотки'}
dictionary(b)

c = {'туфли': 'туфля во множественном числе'}
dictionary(c)



#Задание 4: написать функцию для определения наибольшего числа (реализовать свой max)

def compare(list_):
    max_number = list_[0]
    for i in list_:
        for j in list_:
            if j > i and max_number < j:
                max_number = j
    print(max_number)
compare([1, 5, 2534523, 9, 6, 4, 1456456, 2, 3, 2, 5, 9, 9959])



'''Задание 5: написать функцию, которая извлекает подстроку из строки без 
использования стандартных функций для работы со строкой список задач'''
def search_str(searched, list_exaple):
    index_list_exaple = 0 # позиция в строке s из которой происходит поиск подстроки
    while (index_list_exaple < len(list_exaple)):
        f_is=True # флажок наличия подстроки в строке
        index_searched = 0 # индекс начала сравнения в строке sub
        # цикл поиска подстроки в строке
        while index_searched<len(searched):
            # проверка, не достигнут ли конец строки s
            if (index_list_exaple+index_searched) == len(list_exaple):
                f_is = False
                index_list_exaple = len(list_exaple)-1
                break
            # проверка на несовпадение символов
            if list_exaple[index_list_exaple+index_searched]!=searched[index_searched]:
                f_is = False
                break
            else:
                index_searched = index_searched+1
        # Проверка, все ли символы строки и подстроки совпали
        if f_is:
            return list_exaple[index_list_exaple: index_list_exaple + len(searched)] # если совпали, то вернуть позицию
        else:
            index_list_exaple = index_list_exaple+1 # обработка, если не совпали
    return -1 # если не найдена подстрока, то вернуть -1

s1 = "12 213 321 654 9849 84 654 321 321 854 654121 3546 451621 "
s2 = "654121"
pos = search_str(s2, s1)
print("pos = ", pos)



'''Задание 6: написать функцию, которая находит максимальное значение в списке (без использования функции max) и с 
использованием цикла while'''

list_ = [[[12, 14, 10], [56, 78, 90]], [[56, 32, 1, 10], [-1, 2, 67, 90]], [[100, 102, 56], [78, 65, 43]]]
def max_digit(list_):
    new_list= []
    max_list_= 0
    dlina_spiska = len(list_) # делаю так, только потому, что вижу как выглядит список
    while dlina_spiska > 0:
        for elem in list_: #берём первый эл-т(2списка)
            dlina_spiska -= 1
            for item in elem: # берём один список из 2-ух
                for thing in item: # берём число из списка
                    if thing > max_list_:
                        max_list_ = thing
    print(max_list_)
max_digit(list_)


'''Задача 7: написать функцию, которая принимает список, отфильтровывает нечетные значения 
и возвращает True, если все четные > 0 иначе False'''

list_ = [12, 14, 10, 56, 78, 90, 56, 32, 1, 10, -1, 2, 67, 90, 100, 102, 56, 78, 65, 43]
def even_biger_zero(list_):
    new_list = list(filter(lambda x: x % 2 == 0, list_))
    is_bigger_zero = True
    for number in new_list:
        if number < 0:
            is_bigger_zero = False
    print(is_bigger_zero)
even_biger_zero(list_)


'''Задача 8: написать функцию, которая принимает в себя время в виде "HH:mm:ss" и считает, сколько всего секунд'''

time = "00:02:10"
def convert_in_sec(time):
    time = time.split(sep=':')
    time = [*time]
    sec = 0
    sec = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    print('всего', sec, 'секунд')
convert_in_sec(time)


'''Задача 9: Даны два массива
Надо сделать чтобы значения, а были ключами, а значения b — значениями дикта'''

my_dict = {}
def connect_dict(a, b):
    dlinna_spiska = len(a)
    print(dlinna_spiska)
    for i in range(dlinna_spiska):
        my_dict[a[i]] = b[i]
        print(my_dict)

a = [1, 2, 3]

b = [q, w, e]
connect_dict(a,b)


#Задача 10: Найти три ключа с наибольшими значениями

dict_1 = {'a':500, 'b': 5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
dict_copy = dict_1.copy()
max_item_list = []
for i in range(3):
    dict_2 = dict_copy.items()
    dict_2 = list(dict_2)
    max_item = max(dict_2, key=lambda i: i[1])
    max_item_list.append(max_item[0])
    dict_copy[max_item[0]] = 0
print(max_item_list)