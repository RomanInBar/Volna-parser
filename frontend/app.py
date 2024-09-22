import logging
import tkinter as tk

from frontend.parser_menu import ParserMenu
from frontend.upload_file import UploadFile


class Application(tk.Tk):
    font_size = ("Arial", 12)

    def __init__(self):
        super().__init__()
        self.title("ООО Волна")
        self.put_frames()

    def put_frames(self):
        logging.info("Загрузка фреймов")
        self.replacement = ParserMenu(self).grid(row=0, column=0, sticky=tk.NSEW)
        self.upload_file = UploadFile(self).grid(row=1, column=0, sticky=tk.NSEW)
        logging.info("Загрузка фреймов завершена")

    def refresh(self, f_name: str):
        self.nametowidget(f_name).destroy()
        self.put_frames()
