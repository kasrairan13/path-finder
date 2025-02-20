from sys import argv
from os import listdir, path
from typing import Any, List

from models import Use


class Path:
    def __init__(self):
        self.file_path = path.abspath(argv[0])
        self.current_path = path.dirname(__file__)
        self.paths = [self.current_path]
        self.depth = Use.setup_list["depth"]
        self.excluded_dirs = Use.setup_list["excluded_dirs"]

    def list_dirs(self, base_path: str) -> List[str]:
        return [
            path.join(base_path, directory)
            for directory in listdir(base_path)
            if path.isdir(path.join(base_path, directory)) and
            directory not in self.excluded_dirs
        ]

    def search_dirs(self, base_path: str, current_depth: int = 0):
        if current_depth < self.depth:
            directory = self.list_dirs(base_path)
            self.paths.extend(directory)
            for folder in directory:
                self.search_dirs(folder, current_depth + 1)

    def get_info(self) -> List[Any]:
        self.search_dirs(self.current_path)
        return [self.depth, self.paths, self.current_path, self.file_path]
