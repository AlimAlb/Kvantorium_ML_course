# Домашнее задание
## №1 - склад Ozon
На складе Ozon есть сортировочный конвеер. Его задача фиксировать названия товаров и их количество, которое прошло по конвееру. 

Пример ввода:

    ['Футболка Nike', 'Книга Дж. Оруэлл - 1984', 'Adidas футбольный мяч', 'Книга Дж. Оруэлл - 1984', 'Футболка Nike', 'кроссовки Jordan 1', 'Футболка Nike']

Итогом работы программы должен быть словарь с ключами в виде названия товаров и значениями в виде количества раз, которое этот товар появился на конвеере.

Пример вывода:

    {
        'Книга Дж. Оруэлл - 1984' : 2, 
        'Adidas футбольный мяч' : 1, 
        'Футболка Nike' : 3, 
        'кроссовки Jordan 1' : 1
    }

## №2 - Шифратор/Дешифратор
Напишите программу, которая принимает на вход текст и правило шифрования этого текста, далее выводит шифр в файл "shifr.txt" и уведомить пользователя о том, что текст зашифрован. После программа дожна прочитать шифр из файла и затем дешифровать его. Для сохранения правила шифрования пользуйтесь словарем. Для чтения и записи в файл создавайте отдельные объекты файлов.
Пример ввода:

    I want go to picnic
    I - 1
    to - @
    picnic - ^
    want - !
    go - #
    

Формат вывода (в файл):

    1 ! # @ ^


## №3 - Доступы в файловой системе
У всех файлов в файловой системе есть права и доступы, которые определяют список операций, которые с ними можно совершать. Напишите программу, которая должна определять, какие операции с файлами выполнять можно, а какие нет.

Ваша программа должна считать из файла "access.txt" права доступов к разным файлам, файл выглядит следующим образом:

    script.py W X R
    foto.jpg R
    bot.py W
    video.mp3 R
    file.pdf W R
    document.docx W R

где W - разрешение на запись, X - разрешение на запуск,  R - разрешение на чтение. Если напротив одного файла стоят несколько доступов, то у файла есть все эти доступы.

Программа должна считывать команды в бесконечном цикле(до команды exit) и печатать в консоль о возможности или невозможности выполнения той или иной программы. Формат следующий:

    run script.py
    ...execution started...
    read script.py 
    ...reading allowed...
    write script.py
    ...writing allowed...
    execution file.pdf
    ...access denied...
    write file.pdf
    ...writing allowed...
    read bot.py
    ...access denied...

Где run - запуск файла, read - чтение, write - запись

## №4 - Адреса почты
В базе данных (файл data_base.txt) хранятся адреса почт в следующем формате:

    mgu.edu: andrei_serov, alexander_pushkin, elena_belova, kirill_stepanov
    gmail.com: alena.semyonova, ivan.polekhin, marina_abrabova
    msu.edu: sergei.zharkov, julia_lyubimova, vitaliy.smirnoff
    yandex.ru: ekaterina_ivanova, glebova_nastya,
    harvard.edu: john.doe, mark.zuckerberg, helen_hunt
    mail.ru: roman.kolosov, ilya_gromov, masha.yashkina

Ваша задача - считать все эти данные и вывезти фамили в формате: имя_пользователя@домен
    
    andrei_serov@mgu.edu
    alexandr_pushkin@mgu.edu
    ...
    alena.semyonova@gmail.ru
    ...
    masha.yashkina@mail.ru


## №5 - продолжаем улучшать базу данных
Возьмите свой код с базой данных на словарях и модифицируйте его так, чтобы была возможность модифицировать данные в таблице. Реализуйте так, как предпочитаете нужным, главные требования:
1. Возможность менять весь набор данных в записи
2. Проверка на дубликаты
