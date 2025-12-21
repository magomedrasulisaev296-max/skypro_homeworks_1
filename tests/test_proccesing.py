from src.processing import filter_by_state, sort_by_date

# Тестовые данные
transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-03", "amount": 100},
    {"id": 2, "state": "CANCELED", "date": "2023-01-01", "amount": 200},
    {"id": 3, "state": "EXECUTED", "date": "2023-01-02", "amount": 300},
    {"id": 4, "state": "PENDING", "date": "2023-01-05", "amount": 400},
    {"id": 5, "state": "EXECUTED", "date": "2023-01-04", "amount": 500},
]


# Тесты filter_by_state
def test_filter_executed():
    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 3
    assert [t["id"] for t in result] == [1, 3, 5]
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_canceled():
    result = filter_by_state(transactions, "CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_default():
    result = filter_by_state(transactions)
    assert len(result) == 3
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_empty():
    assert filter_by_state([]) == []


def test_filter_no_match():
    result = filter_by_state(transactions, "INVALID")
    assert result == []


# Тесты sort_by_date
def test_sort_descending():
    result = sort_by_date(transactions)
    assert [t["id"] for t in result] == [4, 5, 1, 3, 2]


def test_sort_ascending():
    result = sort_by_date(transactions, reverse=False)
    assert [t["id"] for t in result] == [2, 3, 1, 5, 4]


def test_sort_empty():
    assert sort_by_date([]) == []


def test_sort_single():
    single = [{"id": 1, "date": "2023-01-01"}]
    result = sort_by_date(single)
    assert result[0]["id"] == 1
