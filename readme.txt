﻿Данная программа предназначена для генерирования автоматов.
Находится в папке Automata. Файл Generator.exe.
При запуске появится окно, в котором
    в строке Count введите число вершин,
    в строке Output file's name имя, в котором необходомо сохранить результат.
    По умолчанию данные сохраняются в файл out.tex.

    После ввода этих данных нажмите CREATE - появятся поля для задания автомата
        в колонке Number можете указать название вершины.
        Если его не указать, то именем будет текущий номер.
        Если вершина начальная или конечная, то поставьте нужный чекбокс.
        Чтобы указать смежные вершины, под нужным номером укажите букву,
            по которой необходимо попасть из одной вершины в другую.
            Если буква не указана, то такого ребра не будет
        Чтобы ввести букву epsilon, напишите 'е' или 'Е'.
    Когда все данные будут введены, нажмите SAVE.

Для изменения:

Bершины могу быть записаны в виде:
    1) \node (start) at (-3.7,1.0){}; - невидимые вершины
    2) \node[circle, draw] (0) at (-2.5,0.0) {0}; - обычная вершина с координатами (-2.5, 0.0)
        Координаты необходимо делать с дробной частью (напр., 0.0)
        {0} - имя, которое будет отображаться
        (0) - имя, с которым данная вершина связана в скрипте
    3) \node [circle, accepting, draw] (3) at (-2.5,0.0) [] {3}; - конечная вершина.
        Чтобы она стала конечной, добавили accepting

Виды ребер:
    1) \draw[->, -latex][loop left] (0) to node[inner sep=0.2pt]{$\varepsilon$} (0); - петля
        [loop left] - петля расположена слева от вершины;
            вместо left можно указать right, above, below. Это поменяет расположение петли
        (0) - петля для вершины 0
        sep=0.2pt - на каком расстоянии от петли должна располагаться буква
        {$\varepsilon$} - буква для петли.
            Если буква не epsilon, то указывается без знаков $ (напр., {a})
    2) \draw [->,-latex] (0) to[bend left=-15, below] node[inner sep=1.3pt] {b} (2); - изогнутая стрелка
        (0) - от какой вершины стрелка
        [bend left=-15, below]
            bend - показывает, что ребро изогнуто
            left - изогнуто влево на -15 единиц. Направление смотрим от основания к стрелке
            below - буква находится под стрелкой. Вместо этого можно указать above, right или left.
        (2) - к какой вершине стрелка
    3) \draw [->,-latex] (0) to node[inner sep=1.3pt] {b} (2); - прямая стрелка
        все как в (2) кроме [bend left=-15, below]. В данном пункте такую скобку не указываем
