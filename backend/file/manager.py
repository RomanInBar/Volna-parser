import logging
import os
from datetime import datetime

import openpyxl


class FileManager:
    """
    Read a loaded file.
    """

    def __init__(self):
        self.filename = f"ООО Радуга {datetime.now().date()}.xlsx"

    @staticmethod
    def read_file(patch: str) -> list[list[str]] | None:
        data = []
        worksheet = openpyxl.load_workbook(patch)
        sheet = worksheet.active
        for row in sheet.rows:
            values = []
            for cell in row:
                if not (value := cell.value):
                    continue
                values.append(value)
            if values:
                data.append(values)
        return data

    def save_file(self, data: list) -> None:
        wb = openpyxl.Workbook()
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
        logging.info("[XLSX] Файл создан")
        worksheet = wb.active
        for row in data:
            worksheet.append(tuple(row))
        logging.info("[XLSX] Данные добавлены")
        wb.save(f"{desktop}\\{self.filename}")
        logging.info("[XLSX] Файл сохранен")
