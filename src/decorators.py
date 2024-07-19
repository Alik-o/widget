from functools import wraps
from typing import Any, Callable, Optional


def log(falename: Optional[str] = None) -> Callable:
    """Логирует вызов функции и записывает результат в файл"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_info = f"{func.__name__} ok\n"
                if falename is None:
                    print(log_info)
                else:
                    with open(falename, "a") as file:
                        file.write(log_info)
                return result
            except Exception as e:
                log_info = f"{func.__name__} error: {e}. Inputs: {args} {kwargs}\n"
                if falename is None:
                    print(log_info)
                else:
                    with open(falename, "a") as file:
                        file.write(log_info)

        return wrapper

    return my_decorator
