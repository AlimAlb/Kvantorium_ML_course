# Домашнее задание
## №1
На прошлом занятии мы писали базу данных на списках. Возьмите код той базы данных и сами добавьте следующие операции:
1. Операция 'show'. Операция должна выводить всю базу данных в виде таблицы(подумайте как это можно сделать, как стоит составлять строки для вывода, чтобы вывод напоминал таблицу)
2. Модифицируйте функцию "add". Добавьте проверку на дубликаты. Если в базе данных уже есть объект, который полностью совпадает с вводимым сейчас - выводите ошибку и не добавляйте элемент. 


## №2 
Функция удаления элемента из массива реализована с помощью метода pop:

    lst.pop(index)
Но, мы легких путей не ищем, поэтому попробуем реализовать эту функцию сами и заодно понять, как эта фукнция работает под капотом. <br />
Допустим у нас есть список

    [1,2,3,4,5]
Чтобы удалить из него элемент с индексом 2 нам нужно по сути просто поочередно перетащить все элементы после него на один индекс назад, чтобы сосед этого элемента заменил своим значением текущий элемент. Алгоритм выглядит следующим образом:

    [1,2,3,4,5]
        |
    перетаскиваем 4 на место 3(элемент с индексом 2)
        |
        v
    [1,2,4,4,5]
        |
    перетаскиваем 5 на место 4
        |
    [1,2,4,5,5]
        |
    удаляем последний элемент
        |
        v
    [1,2,4,5]

Напишите сами функцию удаления элемента по индексу. Можно лишь пользоваться функцией lst.pop() чтобы
удалять последний элемент списка. Остальное нужно реализовать самим.



## №3
Сортировка элементов списка - очень важный алгоритм. Вариантов отсортировать элементы списка великое множество, однако мы рассмотрим один из самых простых и легко реализуемых алгоритмов - сортировка "пузырьком". Суть алгоритма заключается в том, что вы раз за разом проходите по всему массиву и меняете соседние элементы местами, пока весь список не упорядочится.<br /><br />

Для сортировки по возрастанию алгоритм выглядит следующим образом: вы проходитесь по всем элементам списка и если для двух соседних элементов lst[i] и lst[i+1] верно, что lst[i] > lst[i+1] то вы меняете их местами. Так происходит с каждой парой элементов lst[i] и lst[i+1] для i от 0 до len(lst)-1. Пример сортитовки:<br /><br />

    [5,4,8,3,6,10]  
        |  
        v  
    [5,4,8,3,6,10] --> [4,5,8,3,6,10] --> [4,5,3,8,6,10] --> [4,5,3,6,8,10] - первый проход
        |
        v
    [4,5,3,6,8,10] --> [4,5,3,6,8,10] --> [4,3,5,6,8,10] -- второй проход
        |
        v
    [4,3,5,6,8,10] --> [3,4,5,6,8,10] - третий проход, все элементы отсортированы 


Другой пример сортировки пузырком (гифка):
![alt-text](https://github.com/AlimAlb/Kvantorium_ML_course/blob/main/28-dec-22--lists/bubble_sort.gif)


Реализуйте алгоритм сортитовки пузырьком. Напишите программу, которая считывает сначала количество элементов в списке, а затем заданное число элементов в консоли. После - выводит эти элементы в отсортированном порядке. <br />

Кроме отсортированного массива выведите в консоль время затраченное на сортировку. Чтобы посчитать время, потраченное на выполнение программы можно воспользоваться библиотекой *time*

    import time
    start_time = time.time() # текущее время
    #ваш код
    time.sleep(1)
    #имититруем работу вашего кода с помощью функции sleep - которая останавливает кода на 1 секунду
    all_time = time.time() - start_time #текущее время минус время когда программа началась
    print("--- ", all_time,  "seconds ---")

## №4
Используя описанные выше алгоритм сортировки добавьте в базу данных операцию "sort <by_value>", где <br />

    by-value in ["salary", "status"]

 для сортировки базы данных по: зарплате, должности(при сортировке должностей считать, что 'CEO' > 'manager' > 'software_engineer')

