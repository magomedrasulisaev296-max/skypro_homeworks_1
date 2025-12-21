import re
from collections import Counter


def process_bank_search(dict_: list[dict], string_for_search: str) -> list[dict]:
    '''находит операции по описанию "string_for_search"'''
    transactions = []
    re_patern = re.compile(string_for_search, re.IGNORECASE)
    for i in dict_:
        if re_patern.search(str(i.get("description", ""))):
            transactions.append(i)
    return transactions


def process_bank_operations(dict_: list[dict], categories: list) -> dict:
    """ищет операции в списке словарей по заданной категории: categories"""
    transactions = []
    for i in dict_:
        if i["description"] in categories:
            transactions.append(i["description"])
    return dict(Counter(transactions))
