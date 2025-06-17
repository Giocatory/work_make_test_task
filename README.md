# CSV Processor

Простой и расширяемый CLI-инструмент для фильтрации и агрегации данных из CSV-файлов.

## Оглавление

1. [Описание](#описание)  
2. [Требования](#требования)  
3. [Установка](#установка)  
4. [Структура проекта](#структура-проекта)  
5. [Использование](#использование)  
   - [Вывод всех данных](#вывод-всех-данных)  
   - [Фильтрация](#фильтрация)  
   - [Агрегация](#агрегация)  
6. [Опции CLI](#опции-cli)  
7. [Запуск тестов](#запуск-тестов)  

## Описание

Данный скрипт позволяет быстро и удобно:

- Фильтровать строки CSV по любому столбцу (операторы `gt`, `lt`, `eq`).  
- Считать простые статистические агрегаты (`min`, `max`, `avg`) по числовым столбцам.  
- Выводить отфильтрованные данные в виде аккуратной таблицы в терминале.  

## Требования

- Python ≥ 3.7  
- Модуль `tabulate` (для красивого табличного вывода)  
- `pytest` (для запуска юнит-тестов)  

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Giocatory/work_make_test_task
   ```

2. Создайте и активируйте виртуальное окружение (рекомендуется):

   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate.bat    # Windows
   ```
3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Структура проекта

```css
csv_processor/
├── csv_processor/           # Пакет с исходниками
│   ├── __init__.py
│   ├── cli.py               # Точка входа, парсит аргументы и выводит в терминал
│   ├── processor.py         # Логика фильтрации и агрегации
├── tests/                   # Pytest
│   ├── test_processor.py
│   └── test_cli.py
├── requirements.txt         # Список зависимостей
└── README.md               
```

## Использование

Результат:

<img src="https://github.com/Giocatory/work_make_test_task/blob/main/Results.PNG" width=1200 />

### Вывод всех данных

```bash
python -m csv_processor.cli path/to/data.csv
```

Выведет всё содержимое файла как таблицу в формате GitHub:

```css
| name   | price | rating |
| ------ | ----- | ------ |
| item1  | 10    | 4.5    |
| item2  | 20    | 3.7    |
| item3  | 15    | 4.9    |
```

### Фильтрация

```bash
python -m csv_processor.cli data.csv --filter price gt 12
```

* `price` — имя столбца.
* `gt` — оператор (`gt`, `lt`, `eq`).
* `12` — значение для сравнения.

Выведет только строки, где `price > 12`.

### Агрегация

```bash
python -m csv_processor.cli data.csv --filter price gt 12 --agg rating avg
```

Сначала отфильтрует `price > 12`, затем посчитает среднее значение в столбце `rating`:

```
avg(rating) = 4.3
```

Без фильтрации:

```bash
python -m csv_processor.cli data.csv --agg price max
```

Посчитает максимальное значение `price` по всему файлу.


## Опции CLI

```shell
usage: cli.py [-h] [--filter COLUMN OP VALUE] [--agg COLUMN FUNC] file

Простой CSV-процессор: фильтрация и агрегация

positional arguments:
  file                  путь к CSV-файлу

optional arguments:
  -h, --help            показать это сообщение и выйти
  --filter COLUMN OP VALUE
                        Фильтр: COLUMN OPERATOR VALUE
                        OPERATORS: gt, lt, eq
  --agg COLUMN FUNC     Агрегация: COLUMN FUNC
                        FUNCS: min, max, avg
```

## Запуск тестов

Для проверки корректности работы всего функционала запустите:

```bash
pytest
```

* Папка `tests/` уже содержит тесты для `filter_data`, `aggregate_data` и `CLI`.
* Полезные опции:

  * `pytest -q` — краткий отчёт.
  * `pytest --maxfail=1 --disable-warnings -q` — остановиться после первой ошибки.

