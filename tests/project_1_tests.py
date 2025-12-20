from src.project_1 import process_bank_search, process_bank_operations


def test_bank_functions():
    data = [
        {"description": "Payment for groceries", "amount": 100},
        {"description": "Salary transfer", "amount": 200},
        {"description": "Groceries store", "amount": 50},
        {"description": "Transfer to friend", "amount": 75},
        {"description": "Salary bonus", "amount": 150}
    ]

    # process_bank_search
    assert len(process_bank_search(data, "groceries")) == 2
    assert len(process_bank_search(data, "salary")) == 2
    assert len(process_bank_search(data, "transfer")) == 2
    assert process_bank_search(data, "nonexistent") == []
    assert process_bank_search([], "test") == []

    # process_bank_operations
    assert process_bank_operations(data, ["Salary transfer", "Salary bonus", "Groceries store"]) == {
        "Salary transfer": 1, "Salary bonus": 1, "Groceries store": 1}
    assert process_bank_operations(data, ["Salary transfer"]) == {"Salary transfer": 1}
    assert process_bank_operations(data, ["Nonexistent"]) == {}
    assert process_bank_operations([], ["test"]) == {}