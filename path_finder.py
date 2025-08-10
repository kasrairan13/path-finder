from pathlib import Path as path_lib
from sys import path as sys_path
from typing import Generator


__all__ = []


class GitIgnore:
    def __init__(self) -> None:
        self.file_name = ".gitignore"
        self.excluded_dirs = list()

        if self._exists():
            self.main_file = path_lib(__file__).resolve()
            self.main_dir = self.main_file.parent

            self.text = self._open_file()
            self._remove_base_dir()

    def _exists(self) -> bool:
        return path_lib(self.file_name).exists()
    
    def _open_file(self) -> list[str]:
        text = path_lib(self.file_name).read_text()
        return text.splitlines()
    
    def _get_lines(self) -> Generator:
        for line in self.text:
            if "/" in line and not line.startswith("#"):
                yield line

    def _get_dirs(self) -> Generator:
        for directory in self._get_lines():
            directory = directory.split(".")
            if len(directory) >= 2 and "/" not in directory[-1]:
                continue
            yield directory

    def _complete_paths(self) -> Generator:
        for directory in self._get_dirs():
            path = self.main_dir / directory[0]
            yield str(path)

    def _remove_base_dir(self) -> None:
        for directory in self._complete_paths():
            if directory != str(self.main_dir):
                self.excluded_dirs.append(directory)


class Path(GitIgnore):
    def __init__(self) -> None:
        super().__init__()

        self._add()

    def _scan_dirs(self) -> Generator:
        for directory in self.main_dir.rglob('*'):
            directory = str(directory)
            if any(directory.startswith(excluded) for excluded in self.excluded_dirs):
                continue
            yield directory

    def _add(self) -> None:
        for paths in self._scan_dirs():
            sys_path.append(paths)


instance = Path()
