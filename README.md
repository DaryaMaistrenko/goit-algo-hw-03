# goit-algo-hw-03
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Умова:

***Завдання 1:***

Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.

Також візьміть до уваги наступні умови:

1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

2. Рекурсивне читання директорій:

Має бути написана функція, яка приймає шлях до директорії як аргумент.
Функція має перебирати всі елементи у директорії.
Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він має бути доступним для копіювання.


3. Копіювання файлів:

Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.


***Завдання 2:***

Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Критерії прийняття завдань:

***Завдання 1:***

1. Парсинг аргументів. Скрипт приймає два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

2. Рекурсивне читання директорій:

Написана функція, яка приймає шлях до директорії як аргумент.
Функція перебирає всі елементи у директорії.
Якщо елемент є директорією, функція викликає саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він є обробленим для копіювання.
3. Копіювання файлів:

Для кожного типу файлів створюється новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом копіюється у відповідну піддиректорію.
4. Обробка винятків: код обробляє винятки, наприклад, помилки доступу до файлів або директорій.

5. Після виконання програми всі файли у вихідній директорії рекурсивно скопійовано в нову директорію та розсортовано в піддиректорії за їх розширенням.

***Завдання 2:***

1. Код виконується. Програма візуалізує фрактал «сніжинка Коха».

2. Користувач має можливість вказати рівень рекурсії.


