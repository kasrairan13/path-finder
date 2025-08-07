from csv import DictWriter

from validations import Validation


class File:
    def __new__(cls, data: dict, path_data: list[int, str]) -> None:
        instance = super().__new__(cls)

        instance.create_log_file = data["create_log_file"]
        instance.file_name = f"{data["file_name"]}.csv"
        instance.header = data["header"]
        instance.path_data = path_data

        if instance.create_log_file:
            instance._write_row()
        
        return instance

    def _file_exist(self) -> None:
        if not Validation.file_exists(self.file_name):
            with open(self.file_name, mode="w") as file:
                csv_file = DictWriter(file, fieldnames=self.header)
                csv_file.writeheader()
    
    def _create_row(self) -> dict:
        return dict(zip(self.header, self.path_data))

    def _write_row(self) -> None:
        self._file_exist()
        with open(self.file_name, mode="a") as file:
            csv_file = DictWriter(file, fieldnames=self.header)
            csv_file.writerow(self._create_row())
