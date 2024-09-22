from typing import Callable

from backend.file.manager import FileManager
from backend.parser.replacing import Replace
from backend.parser.scrape import Scrape


class Scripts:
    parser: Scrape = Scrape()
    replace: Replace = Replace()
    file: FileManager = FileManager()

    def _save_change_data(self, data: list[list[str]]) -> None:
        modified_data = self.replace.replacing(data)
        self.file.save_file(modified_data)

    def start_file_scripts(self, patch: str, callback: Callable[[str], None]) -> None:
        data_from_file = self.file.read_file(patch=patch)
        if data_from_file:
            self._save_change_data(data_from_file)
        callback(f"Файл создан и скачен на рабочий стол {self.file.filename}")

    def start_parser_scripts(self, callback: Callable[[str], None]) -> None:
        data_from_url = self.parser.get_data_from_urls()
        self._save_change_data(data_from_url)
        callback(f"Файл создан и скачен на рабочий стол {self.file.filename}")


scripts = Scripts()
