from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)  # ← ДОБАВЬ ЭТУ СТРОКУ
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            msg = f"{func.__name__} started"
            if filename:
                with open(filename, "a") as f:
                    f.write(msg + "\n")
            else:
                print(msg)
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} finished"
                if filename:
                    with open(filename, "a") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)
                return result
            except Exception as e:
                error_msg = (
                    f"{func.__name__} raised {type(e).__name__} with args: {args}, kwargs: {kwargs}. Error: {str(e)}"
                )
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_msg + "\n")
                else:
                    print(error_msg)
                raise

        return wrapper

    return decorator
