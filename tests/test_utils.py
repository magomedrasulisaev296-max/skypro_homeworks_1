import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_transactions():
    # Тест 1: Успешная загрузка
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with (
        patch("builtins.open", mock_open(read_data=json.dumps(mock_data))),
        patch("os.path.exists", return_value=True),
        patch("os.path.abspath", return_value="/test/path"),
        patch("builtins.print"),
    ):
        result = load_transactions("test.json")
        assert result == mock_data

    # Тест 2: Файл не найден
    with (
        patch("os.path.exists", return_value=False),
        patch("os.path.abspath", return_value="/test/path"),
        patch("builtins.print"),
    ):
        result = load_transactions("nonexistent.json")
        assert result == []

    # Тест 3: Некорректный JSON
    with (
        patch("builtins.open", mock_open(read_data="invalid json")),
        patch("os.path.exists", return_value=True),
        patch("builtins.print"),
    ):
        result = load_transactions("bad.json")
        assert result == []

    # Тест 4: JSON не список
    with (
        patch("builtins.open", mock_open(read_data=json.dumps({"key": "value"}))),
        patch("os.path.exists", return_value=True),
        patch("builtins.print"),
    ):
        result = load_transactions("not_list.json")
        assert result == []

    # Тест 5: Пустой файл
    with (
        patch("builtins.open", mock_open(read_data="")),
        patch("os.path.exists", return_value=True),
        patch("builtins.print"),
    ):
        result = load_transactions("empty.json")
        assert result == []

    # Тест 6: Ошибка при чтении файла
    with (
        patch("builtins.open", side_effect=PermissionError("Access denied")),
        patch("os.path.exists", return_value=True),
        patch("builtins.print"),
    ):
        result = load_transactions("protected.json")
        assert result == []

    # Тест 7: Успешная загрузка с путем
    mock_data = [{"id": 3}]
    with (
        patch("builtins.open", mock_open(read_data=json.dumps(mock_data))),
        patch("os.path.exists", return_value=True),
        patch("builtins.print"),
    ):
        result = load_transactions("/full/path/to/data.json")
        assert result == mock_data

    # Тест 8: Пустой список
    with (
        patch("builtins.open", mock_open(read_data=json.dumps([]))),
        patch("os.path.exists", return_value=True),
        patch("builtins.print"),
    ):
        result = load_transactions("empty_list.json")
        assert result == []
