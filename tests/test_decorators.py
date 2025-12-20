import unittest
import os
import tempfile
from unittest.mock import patch
from src.decorators import log


class TestLogDecorator(unittest.TestCase):

    def test_log_without_filename_prints_to_stdout(self):
        @log()
        def test_func():
            return "test"

        with patch('builtins.print') as mock_print:
            result = test_func()
            self.assertEqual(result, "test")
            self.assertEqual(mock_print.call_count, 2)

    def test_log_with_filename_writes_to_file(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
            tmp_filename = tmp_file.name

        try:
            @log(filename=tmp_filename)
            def test_func():
                return "file_test"

            result = test_func()
            self.assertEqual(result, "file_test")

            with open(tmp_filename, 'r') as f:
                content = f.read()

            self.assertIn('test_func started', content)
            self.assertIn('test_func finished', content)

        finally:
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)

    def test_log_preserves_function_name_and_docstring(self):
        @log()
        def original_function():
            """Это документация оригинальной функции"""
            return "preserved"

        self.assertEqual(original_function.__name__, 'original_function')
        self.assertEqual(original_function.__doc__, 'Это документация оригинальной функции')

    def test_log_with_exception(self):
        @log()
        def failing_func():
            raise ValueError("Test error")

        with patch('builtins.print') as mock_print:
            with self.assertRaises(ValueError):
                failing_func()

            self.assertEqual(mock_print.call_count, 2)
            error_message = mock_print.call_args_list[1][0][0]
            self.assertIn('raised ValueError', error_message)

    def test_log_with_args_and_kwargs(self):
        @log()
        def multiply(a: int, b: int, multiplier: int = 1) -> int:
            return a * b * multiplier

        with patch('builtins.print') as mock_print:
            result = multiply(2, 3, multiplier=4)
            self.assertEqual(result, 24)

            @log()
            def failing_with_args(x, y=0):
                raise TypeError("Arg test")

            with self.assertRaises(TypeError):
                failing_with_args("arg1", y="arg2")

            for call in mock_print.call_args_list:
                if 'raised' in call[0][0]:
                    error_message = call[0][0]
                    self.assertIn('arg1', error_message)
                    self.assertIn("'y': 'arg2'", error_message)  # ← ИСПРАВЛЕНО

    def test_log_with_filename_and_exception(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
            tmp_filename = tmp_file.name

        try:
            @log(filename=tmp_filename)
            def failing_func():
                raise RuntimeError("File error test")

            with self.assertRaises(RuntimeError):
                failing_func()

            with open(tmp_filename, 'r') as f:
                content = f.read()

            self.assertIn('raised RuntimeError', content)

        finally:
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)

    def test_log_decorator_returns_correct_value(self):
        @log()
        def add(a: int, b: int) -> int:
            return a + b

        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_log_multiple_functions(self):
        @log()
        def func1():
            return "func1"

        @log()
        def func2():
            return "func2"

        with patch('builtins.print') as mock_print:
            result1 = func1()
            result2 = func2()

            self.assertEqual(result1, "func1")
            self.assertEqual(result2, "func2")
            self.assertEqual(mock_print.call_count, 4)