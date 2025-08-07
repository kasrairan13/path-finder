from os import path
from typing import Any, get_origin, get_args
from re import match


class Validation:
    @staticmethod
    def file_exists(name: str) -> bool:
        return path.exists(name)
    
    @staticmethod
    def check_file_name(name: Any) -> bool:
        pattern = r"^[\w .-]{1,200}$"
        return bool(match(pattern, name))
    
    @staticmethod
    def check_items(value, _type) -> bool:
        return isinstance(value, tuple) and all(isinstance(item, _type) for item in value)
    
    @staticmethod
    def is_collection_of(
        value: Any,
        type_hint: type,
        container_type: type,
        element_type: Any
    ) -> bool:
        origin = get_origin(type_hint)
        args = get_args(type_hint)
        return (
            origin == container_type and
            args == (element_type,) and
            Validation.check_items(value, args)
        )


class DataValidation:
    def __new__(cls, *args: tuple[str, Any, type]):
        instance = super().__new__(cls)
        instance.valid = instance._valid(*args)
        return instance.valid
    
    def _valid(self, *args: tuple[Any, type]) -> list[str, bool]:
        list_state = list()
        for name, value, type_hint in args:
            if get_origin(type_hint) is not None:
                state = Validation.is_collection_of(value, type_hint, tuple, str)
            elif name == "file_name":
                state = Validation.check_file_name(value)
            else:
                state = isinstance(value, type_hint)
            list_state.append((name, state))
        return list_state
