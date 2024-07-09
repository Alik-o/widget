from src.decorators import log


def test_log_():
    @log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(2, 3)
    assert result == 5


def test_decorator_log(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    add_numbers(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n\n"


def test_log_error(capsys):
    @log()
    def division_numbers(a, b):
        return a / b

    division_numbers(5, 0)
    captured = capsys.readouterr()
    assert captured.out == "division_numbers error: division by zero. Inputs: (5, 0) {}\n\n"
