Программа получает данные с сайта hh.ru, проектирует таблицу в БД PostgreSQL и загрузить полученные данные в созданные таблицы.


Для работы программы необходимо установить зависимости, указанные в файле pyproject.toml


Для работы с базой данных необходимо создать файл database.ini с параметрами доступа к базе данных PostgresSQL. Пример содержимого файла:

[postgresql]
host=localhost
user=postgres
password=000
port=5432

Описание файлов

    main.py содержит функцию main, которая запускает цепочку действий по сбору данных с сайта hh.ru и записи ее в базу данных PostgresSQL.
    api_hh.py класс для работы с платформой hh.ru
    utils.py содержит функцию create_database() для создания базы данных и функцию save_data_to_database() для сохранения данных
    dbmanager.py содержит класс DBManager, который позволяет работать с базой данных PostgresSQL.
