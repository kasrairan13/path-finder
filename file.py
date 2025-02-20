from csv import DictWriter

from models import Use
from path import Path
from validation import Validation


class File:
    def __init__(self):
        self.path = Path()
        self.validation = Validation()
        self.file_name = f"{Use.setup_list['file_name']}.csv"
        self.header = Use.setup_list["header"]

    def file_exist(self):
        if not self.validation.file_exists(self.file_name):
            with open(self.file_name, mode="w") as file:
                csv_file = DictWriter(file, fieldnames=self.header)
                csv_file.writeheader()
    
    def create_row(self) -> dict:
        return dict(zip(self.header, self.path.get_info()))
    
    def write_row(self):
        self.file_exist()
        with open(self.file_name, mode="a") as file:
            csv_file = DictWriter(file, fieldnames=self.header)
            csv_file.writerow(self.create_row())
