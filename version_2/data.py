from dataclasses import dataclass, field, asdict

from validations import DataValidation
from errors import DataError


@dataclass()
class Data:
    depth: int = 2
    create_log_file: bool = True
    file_name: str = "log"  # format csv
    header: list[str] = field(init=False)
    excluded_dirs: tuple[str] = None

    def __post_init__(self) -> None:
        self.header = ["depth", "paths", "main_folder", "main_file"]
        list_state = DataValidation(
            ("depth", self.depth, int),
            ("create_log_file", self.create_log_file, bool),
            ("file_name", self.file_name, str),
            ("excluded_dirs", self.excluded_dirs, tuple[str])
        )
        DataError(*list_state)


def get_data(instance: Data) -> dict:
    return asdict(instance)
