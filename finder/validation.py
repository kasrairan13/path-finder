from os import path


class Validation:
    @staticmethod
    def file_exists(name: str) -> bool:
        return path.exists(name)
    
    @staticmethod
    def is_int(value) -> bool:
        return isinstance(value, int)
    
    @staticmethod
    def is_str(value) -> bool:
        return isinstance(value, str)
    
    @staticmethod
    def is_list_str(value) -> bool:
        return isinstance(value, list) and all(isinstance(item, str) for item in value)
