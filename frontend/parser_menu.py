import logging
import tkinter as tk
from tkinter import messagebox, ttk

from backend.app import scripts
from database.manager import DBManager
from database.models import Replacement
from database.schemas import ReplaceSchema
from frontend.tooltip import CustomTooltip


class ParserMenu(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.width_buttons = 25
        self.width_entry = 35
        self.objects = DBManager(Replacement)
        self.put_widgets()

    def put_widgets(self):
        logging.info(f"Загрузка виджетов {self.__class__.__name__}")
        self.old_value_text = tk.Label(
            self, text="Текущее значение", font=self.parent.font_size
        )
        self.old_value_text.grid(row=0, column=0, sticky=tk.W)
        self.old_value_input = tk.Entry(self, width=25)
        self.old_value_input.grid(row=1, column=0, sticky=tk.W)
        CustomTooltip(
            self.old_value_input, "Запишите сюда слово, которое хотите поменять"
        )

        self.new_value_text = tk.Label(
            self, text="Новое значение", font=self.parent.font_size
        )
        self.new_value_text.grid(row=0, column=1, sticky=tk.W)
        self.new_value_input = tk.Entry(self, width=25)
        self.new_value_input.grid(row=1, column=1, sticky=tk.W)
        CustomTooltip(
            self.new_value_input,
            "Запишите сюда новое слово,\nоно заменит собой то, которое вы хотите поменять",
        )

        self.list_values_text = tk.Label(
            self, text="Список заменяемых слов", font=self.parent.font_size
        )
        self.list_values_text.grid(row=2, column=0, sticky=tk.W)

        values = [ReplaceSchema.values(obj) for obj in self.objects.get_all()]
        heads = ["Заменяемое слово", "Замена"]
        self.table = ttk.Treeview(self, show="headings")
        self.table["columns"] = heads
        for header in heads:
            self.table.heading(header, text=header, anchor="center")
        for row in values:
            self.table.insert("", tk.END, values=row)
        scroll_pane = ttk.Scrollbar(self, command=self.table.yview)
        scroll_pane.grid(row=3, column=2, sticky="ens")
        self.table.configure(yscrollcommand=scroll_pane.set)
        self.table.grid(row=3, column=0, columnspan=3, sticky=tk.NSEW)

        self.start_button = tk.Button(
            self,
            text="Запуск",
            command=self.start,
            width=self.width_buttons,
            font=self.parent.font_size,
        )
        self.start_button.grid(row=4, column=0, sticky=tk.W, pady=15)
        CustomTooltip(self.start_button, "Запускает программу", height=30)

        self.add_button = tk.Button(
            self,
            text="Добавить",
            command=self.add_values,
            width=self.width_buttons,
            font=self.parent.font_size,
        )
        self.add_button.grid(row=4, column=1)
        CustomTooltip(
            self.add_button, "Добавить новую замену слова в список", height=30, width=5
        )

        self.del_button = tk.Button(
            self,
            text="Удалить",
            command=self.delete_value,
            width=self.width_buttons,
            font=self.parent.font_size,
        )
        self.del_button.grid(row=4, column=2)
        CustomTooltip(
            self.del_button, "Удалить замену слова из списка", height=30, width=15
        )
        logging.info(f"Загрузка виджетов {self.__class__.__name__} завершена")

    def add_values(self):
        logging.info("Инициализация добавления значений в базу данных")
        try:
            old_value = self.old_value_input.get()
            new_value = self.new_value_input.get()
            assert old_value and new_value
            self.objects.create(current_value=old_value, replace=new_value)
            logging.info("Добавление завершено")
            self.parent.refresh(self._name)
        except AssertionError:
            msg = "Вы забыли внести данные!"
            messagebox.showwarning(title="Нет данных", message=msg)

    def delete_value(self):
        logging.info("Инициализация удаления значений из базы данных")
        try:
            removed = self.table.selection()[0]
            assert removed
            old_value, new_value = self.table.item(removed)["values"]
            self.objects.remove(current_value=old_value)
            logging.info("Удаление завершено")
            self.parent.refresh(self._name)
        except AssertionError:
            msg = "Ни одной записи не выбрано!"
            messagebox.showwarning(title="Нет данных", message=msg)

    @staticmethod
    def show_result_window(msg):
        """Return a window with a message after script work."""
        messagebox.showinfo(message=msg)

    def start(self):
        if self.parent.file_patch:
            logging.info(
                f"Запуск считывания данных из файла {self.parent.file_patch.endswith}"
            )
            scripts.start_file_scripts(
                patch=self.parent.file_patch, callback=self.show_result_window
            )
            self.parent.file_patch = None
        else:
            logging.info("Запуск парсера")
            scripts.start_parser_scripts(callback=self.show_result_window)
            logging.info("Процесс парсинга завершен")
        self.parent.put_frames()
