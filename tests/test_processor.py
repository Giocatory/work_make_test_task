import pytest
from csv_processor.processor import filter_data, aggregate_data

@pytest.fixture
def sample_data():
    return [
        {'name':'a', 'price':'10', 'rating':'4.5'},
        {'name':'b', 'price':'20', 'rating':'3.7'},
        {'name':'c', 'price':'15', 'rating':'4.9'},
    ]

def test_filter_gt_numeric(sample_data):
    res = filter_data(sample_data, 'price', 'gt', '12')
    assert len(res) == 2
    assert all(float(r['price']) > 12 for r in res)

def test_filter_eq_text():
    data = [
        {'name':'foo', 'brand':'X'},
        {'name':'bar', 'brand':'Y'},
    ]
    res = filter_data(data, 'brand', 'eq', 'X')
    assert res == [{'name':'foo', 'brand':'X'}]

def test_aggregate_min(sample_data):
    assert aggregate_data(sample_data, 'price', 'min') == 10.0

def test_aggregate_max(sample_data):
    assert aggregate_data(sample_data, 'price', 'max') == 20.0

def test_aggregate_avg(sample_data):
    assert aggregate_data(sample_data, 'rating', 'avg') == pytest.approx((4.5 + 3.7 + 4.9) / 3)
