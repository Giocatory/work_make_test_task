from typing import List, Dict, Any
import operator

# Поддерживаемые операции фильтрации
OPS = {
    'eq': operator.eq,   # равно
    'lt': operator.lt,   # меньше
    'gt': operator.gt,   # больше
}

# Поддерживаемые агрегаты
AGG_FUNCS = {
    'min': min,
    'max': max,
    'avg': lambda vals: sum(vals) / len(vals) if vals else None,
}

def filter_data(
    data: List[Dict[str, Any]],
    column: str,
    op_str: str,
    value: Any
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по column OPERATOR value.
    Поддерживает текстовые и числовые колонки.
    """
    if op_str not in OPS:
        raise ValueError(f"Неподдерживаемый оператор: {op_str}")
    op = OPS[op_str]
    result = []
    for row in data:
        cell = row.get(column)
        if cell is None:
            continue
        # пытаемся сравнить как числа, иначе как строки
        try:
            cell_val = float(cell)
            comp_val = float(value)
        except ValueError:
            cell_val = cell
            comp_val = value
        if op(cell_val, comp_val):
            result.append(row)
    return result

def aggregate_data(
    data: List[Dict[str, Any]],
    column: str,
    agg_str: str
) -> float:
    """
    Вычисляет агрегат (min, max, avg) для числовой колонки.
    """
    if agg_str not in AGG_FUNCS:
        raise ValueError(f"Неподдерживаемая агрегация: {agg_str}")
    # приводим все значения колонки к float
    values = [float(row[column]) for row in data]
    return AGG_FUNCS[agg_str](values)
