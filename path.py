from pathlib import Path as path_lib
from sys import path as sys_path
from typing import Generator


__all__ = []


class GitIgnore:
    def __init__(self) -> None:
        self.file_name = ".gitignore"
        self.excluded_dirs = list()

        if self.exists():
            self.main_file = path_lib(__file__).resolve()
            self.main_folder = self.main_file.parent

            self.text = self.open_file()
            self.lines = self.get_lines(self.text)
            self.dirs = self.get_dirs(self.lines)
            self.exc_dirs = self.complete_paths(self.dirs)
            self.remove_base_folder(self.exc_dirs)

    def exists(self) -> bool:
        return path_lib(self.file_name).exists()
    
    def open_file(self) -> list[str]:
        text = path_lib(self.file_name).read_text()
        return text.splitlines()
    
    def get_lines(self, list_lines: list[str]) -> Generator:
        for line in list_lines:
            if "/" in line and not line.startswith("#"):
                yield line

    def get_dirs(self, valid_lines: Generator) -> Generator:
        for directory in valid_lines:
            directory = directory.split(".")
            if len(directory) >= 2 and "/" not in directory[-1]:
                continue
            yield directory

    def complete_paths(self, dirs: Generator) -> Generator:
        for directory in dirs:
            path = f"{self.main_folder / directory[0]}"
            yield path

    def remove_base_folder(self, excluded_dirs: Generator) -> None:
        new_list = list()
        for directory in excluded_dirs:
            if directory != str(self.main_folder):
                new_list.append(directory)
        self.excluded_dirs = new_list


class Path(GitIgnore):
    def __init__(self) -> None:
        super().__init__()

        self.list_dirs = list()
        self.scan_dirs()
        self.add(self.list_dirs)

    def scan_dirs(self) -> None:
        for directory in self.main_folder.rglob('*'):
            directory = str(directory)
            if any(directory.startswith(excluded) for excluded in self.excluded_dirs):
                continue
            self.list_dirs.append(directory)

    def add(self, paths: list[str]) -> None:
        sys_path.extend(paths)


instance = Path()
