from data import Data, get_data
from path import Path
from file import File


def setup(
        depth: int,
        create_log_file: bool,
        file_name: str,
        excluded_dirs: tuple[str],
) -> None:
    data = Data(depth, create_log_file, file_name, excluded_dirs)
    path_data = Path(depth, excluded_dirs)
    File(get_data(data), path_data)
