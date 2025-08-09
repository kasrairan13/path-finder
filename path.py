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
            self.remove_base_folder()

    def exists(self) -> bool:
        return path_lib(self.file_name).exists()
    
    def open_file(self) -> list[str]:
        text = path_lib(self.file_name).read_text()
        return text.splitlines()
    
    def get_lines(self) -> Generator:
        for line in self.text:
            if "/" in line and not line.startswith("#"):
                yield line

    def get_dirs(self) -> Generator:
        for directory in self.get_lines():
            directory = directory.split(".")
            if len(directory) >= 2 and "/" not in directory[-1]:
                continue
            yield directory

    def complete_paths(self) -> Generator:
        for directory in self.get_dirs():
            path = self.main_folder / directory[0]
            yield str(path)

    def remove_base_folder(self) -> None:
        for directory in self.complete_paths():
            if directory != str(self.main_folder):
                self.excluded_dirs.append(directory)


class Path(GitIgnore):
    def __init__(self) -> None:
        super().__init__()

        self.add()

    def scan_dirs(self) -> Generator:
        for directory in self.main_folder.rglob('*'):
            directory = str(directory)
            if any(directory.startswith(excluded) for excluded in self.excluded_dirs):
                continue
            yield directory

    def add(self) -> None:
        for paths in self.scan_dirs():
            sys_path.append(paths)


instance = Path()
