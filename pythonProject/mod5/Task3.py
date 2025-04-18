from typing import Collection, Type, Literal
from types import TracebackType


class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors = errors

    def __enter__(self) -> None:
        pass

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if exc_type in self.errors:
            return True
        elif issubclass(exc_type, *self.errors):
            return True

if __name__ == '__main__':
    err_types = {ZeroDivisionError, TypeError}
    with BlockErrors(err_types):
        result = 1 / 0
    print('Выполнено без ошибок')