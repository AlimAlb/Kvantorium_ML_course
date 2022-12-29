# Домашнее задание
## №1
Сортировка элементов списка - очень важный алгоритм. Вариантов отсортировать элементы списка великое множество, однако мы рассмотрим один из самых простых и легко реализуемых алгоритмов - сортировка "пузырьком". 
 
Суть алгоритма заключается в том, что вы раз за разом проходите по всему массиву и меняется соседние элементы местами, пока весь список не упорядочится. Пример сортитовки:   
[5,4,8,3,6,10]  
    |  
    |  
    v  
[5,4,8,3,6,10] --> [4,5,8,3,6,10] --> [4,5,3,8,6,10] --> [4,5,3,6,8,10] - первый проход 
    | 
    | 
    v 
[4,5,3,6,8,10] --> [4,5,3,6,8,10] --> [4,3,5,6,8,10] -- второй проход 
    | 
    | 
    v 
[4,3,5,6,8,10] --> [3,4,5,6,8,10] - третий проход, все элементы отсортированы 
 
Другой пример сортировки пузырком:
![alt-text](https://github.com/AlimAlb/Kvantorium_ML_course/blob/main/bubble_sort.gif)