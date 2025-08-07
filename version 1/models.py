from sys import path
from typing import List

from file import File
from path import Path
from validation import Validation


class Use:
    setup_list = {
        "depth": 2,
        "excluded_dirs": [],
        "file_name": "log",
        "header": ["depth", "paths", "main_folder", "main_file"]
    }

    @staticmethod
    def setup(
            *,
            depth: int,
            excluded_dirs: List[str],
            file_name: str,
            header: List[str]
    ):
        validation = Validation()
        if not (
            validation.is_int(depth) and
            validation.is_list_str(excluded_dirs) and
            validation.is_str(file_name) and
            validation.is_list_str(header) and
            len(header) == 4
        ):
            raise ValueError("Invalid argument type passed to Use.setup")
        Use.setup_list.update({
            "depth": depth,
            "excluded_dirs": excluded_dirs,
            "file_name": file_name,
            "header": header
        })

    @staticmethod
    def run():
        path_class = Path()
        file_class = File()
        list_path = path_class.get_info()
        file_class.write_row()
        path.extend(list_path[1])
