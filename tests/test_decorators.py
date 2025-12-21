import os
import tempfile
import unittest
from unittest.mock import patch, mock_open, call
from src.decorators import log


class TestLogDecorator(unittest.TestCase):

    def test_log_without_filename(self):
        """Тест 1: Логирование без файла (print)"""

        @log()
        def test_func():
            return "result"

        with patch('builtins.print') as mock_print:
            result = test_func()
            self.assertEqual(result, "result")
            mock_print.assert_has_calls([
                call("test_func started"),
                call("test_func finished")
            ])

    def test_log_with_filename(self):
        """Тест 2: Логирование в файл"""

        @log(filename="test.log")
        def test_func():
            return "result"

        # Мокаем open и проверяем запись
        with patch('builtins.open', mock_open()) as mock_file:
            result = test_func()
            self.assertEqual(result, "result")

            # Проверяем что файл открывался для добавления
            mock_file.assert_called_with("test.log", 'a')

            # Проверяем запись двух сообщений
            handle = mock_file()
            write_calls = handle.write.call_args_list
            self.assertIn("test_func started", write_calls[0][0][0])
            self.assertIn("test_func finished", write_calls[1][0][0])

    def test_log_with_exception_no_file(self):
        """Тест 3: Исключение без файла"""

        @log()
        def test_func():
            raise ValueError("test error")

        with patch('builtins.print') as mock_print:
            with self.assertRaises(ValueError):
                test_func()

            # Проверяем что было 2 print (started + error)
            self.assertEqual(mock_print.call_count, 2)
            error_msg = mock_print.call_args_list[1][0][0]
            self.assertIn("raised ValueError", error_msg)
            self.assertIn("test error", error_msg)

    def test_log_with_exception_and_file(self):
        """Тест 4: Исключение с файлом"""

        @log(filename="error.log")
        def test_func(x, y=0):
            raise RuntimeError("error")

        with patch('builtins.open', mock_open()) as mock_file:
            with self.assertRaises(RuntimeError):
                test_func("arg", y="kwarg")

            handle = mock_file()
            # Проверяем что последнее сообщение содержит информацию об ошибке
            last_write = handle.write.call_args_list[-1][0][0]
            self.assertIn("raised RuntimeError", last_write)
            self.assertIn("arg", last_write)
            self.assertIn("'y': 'kwarg'", last_write)

    def test_log_preserves_metadata(self):
        """Тест 5: Сохранение метаданных"""

        @log()
        def original():
            """Docstring"""
            return "data"

        self.assertEqual(original.__name__, "original")
        self.assertEqual(original.__doc__, "Docstring")
        self.assertEqual(original(), "data")

    def test_log_multiple_calls(self):
        """Тест 6: Множественные вызовы"""

        @log()
        def counter():
            return 1

        with patch('builtins.print') as mock_print:
            self.assertEqual(counter(), 1)
            self.assertEqual(counter(), 1)
            # 2 вызова × 2 сообщения = 4 print
            self.assertEqual(mock_print.call_count, 4)

    def test_log_with_args(self):
        """Тест 7: Функция с аргументами"""

        @log()
        def add(a, b):
            return a + b

        with patch('builtins.print'):
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(10, 20), 30)

    def test_log_filename_none(self):
        """Тест 8: filename=None работает как без файла"""

        @log(filename=None)
        def test_func():
            return "test"

        with patch('builtins.print') as mock_print:
            result = test_func()
            self.assertEqual(result, "test")
            self.assertEqual(mock_print.call_count, 2)

    def test_log_empty_filename_string(self):
        """Тест 9: Пустая строка как filename"""

        @log(filename="")
        def test_func():
            return "empty"

        with patch('builtins.open') as mock_open_func:
            # С пустой строкой не должен открывать файл
            result = test_func()
            self.assertEqual(result, "empty")
            mock_open_func.assert_not_called()