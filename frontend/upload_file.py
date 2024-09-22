import logging
import tkinter as tk
from tkinter.filedialog import askopenfile

from frontend.tooltip import CustomTooltip


class UploadFile(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.file_patch = None
        self.put_widgets()

    def _get_patch_of_file(self):
        try:
            self.parent.file_patch = askopenfile(
                mode="r", filetypes=[("Table files", "*xlsx")]
            ).name
        except AttributeError:
            pass
        else:
            logging.info("Путь к файлу записан")
            self.upload_button["text"] = "Файл загружен"
            self.patch_text = tk.Label(self, text=self.parent.file_patch)
            self.patch_text.grid(row=0, column=5, sticky=tk.W)
            self.update_idletasks()

    def put_widgets(self):
        logging.info(f"Загрузка виджетов {self.__class__.__name__}")
        self.upload_button = tk.Button(
            self,
            text="Загрузить файл",
            command=self._get_patch_of_file,
            width=20,
            font=self.parent.font_size,
        )
        self.upload_button.grid(row=0, column=3, columnspan=2, pady=5, sticky=tk.W)
        CustomTooltip(
            self.upload_button,
            "Загрузить фай для обработки и изменения названий",
            height=340,
            width=25,
        )
        logging.info(f"Загрузка виджетов {self.__class__.__name__} завершена")
