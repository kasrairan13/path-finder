from pathlib import Path as lib_path
from functools import cache
from sys import path as sys_path


class Path:
    def __new__(cls, depth: int, excluded_dirs: tuple[str]) -> list[str, int]:
        instance = super().__new__(cls)

        instance.depth = depth
        instance.excluded_dirs = excluded_dirs
        instance.main_file = lib_path(__file__).resolve()
        instance.main_folder = instance.main_file.parent
        instance.paths = list()

        instance._search_dirs(instance.main_folder)
        instance._add_paths(instance.paths)

        return [instance.depth, instance.paths, instance.main_file, instance.main_folder]

    def _list_dirs(self, base_path: lib_path) -> list[lib_path]:
        list_path = list()
        dirs = base_path.iterdir()
        for dir in dirs:
            if dir.is_dir() and dir.name not in self.excluded_dirs:
                list_path.append(dir)
        return list_path
    
    @cache
    def _search_dirs(self, base_path: lib_path, current_depth: int = 0) -> None:
        if current_depth < self.depth:
            dirs = self._list_dirs(base_path)
            self.paths.extend(dirs)
            for dir in dirs:
                self._search_dirs(dir, current_depth + 1)
    
    def _add_paths(self, paths: list[lib_path]) -> None:
        for path in paths:
            sys_path.append(str(path))
