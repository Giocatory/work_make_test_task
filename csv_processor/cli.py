import argparse
import csv
from tabulate import tabulate
from .processor import filter_data, aggregate_data

def parse_args():
    parser = argparse.ArgumentParser(
        description="Простой CSV-процессор: фильтрация и агрегация"
    )
    parser.add_argument('file', help="Путь к CSV-файлу")
    parser.add_argument(
        '--filter',
        nargs=3, metavar=('COLUMN','OP','VALUE'),
        help="Фильтр: COLUMN OPERATOR VALUE; OPERATORS: gt, lt, eq"
    )
    parser.add_argument(
        '--agg',
        nargs=2, metavar=('COLUMN','FUNC'),
        help="Агрегация: COLUMN FUNC; FUNCS: min, max, avg"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    # Чтение CSV
    try:
        with open(args.file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return

    # Фильтрация (если есть)
    if args.filter:
        col, op, val = args.filter
        try:
            data = filter_data(data, col, op, val)
        except ValueError as e:
            print(f"❌ {e}")
            return

    # Агрегация (если есть) — выводим только число
    if args.agg:
        col, func = args.agg
        try:
            result = aggregate_data(data, col, func)
        except Exception as e:
            print(f"❌ {e}")
            return
        print(f"{func}({col}) = {result}")
    else:
        # Просто табличка с выборкой
        if data:
            print(tabulate(data, headers="keys", tablefmt="github", floatfmt=".4g"))
        else:
            print("ℹ️  Нет данных для отображения.")

if __name__ == "__main__":
    main()
