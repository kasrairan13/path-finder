from typing import Any


class Error:
    @staticmethod
    def raise_value_error(text: str, *args: Any):
        text = f"{text} {args}"
        raise ValueError(text)


class DataError():
    def __new__(cls, *args: tuple[str, bool]):
        instance = super().__new__(cls)
        instance.check_value = instance._check_value(*args)
        return instance.check_value
    
    def _check_value(self, *args: tuple[str, bool]):
        invalid_values = list()
        for name, state in args:
            if not state:
                invalid_values.append(name)
        if invalid_values:
            Error.raise_value_error("Invalid Values:", *invalid_values)
