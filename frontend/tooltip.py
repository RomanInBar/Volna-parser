import tkinter as tk


class CustomTooltip:
    def __init__(self, widget: tk.Widget, text: str, width: int = 50, height: int = 20):
        self.widget = widget
        self.text = text
        self.tooltip_visible: bool = False
        self.width = width
        self.height = height

        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if not self.tooltip_visible:
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_x() + self.width
            y += self.widget.winfo_y() + self.height
            self.tooltip_label = tk.Label(
                text=self.text, background="lightyellow", relief="solid", borderwidth=1
            )
            self.tooltip_label.place(x=x, y=y)
            self.tooltip_visible = True

    def hide_tooltip(self, event=None):
        if self.tooltip_visible:
            self.tooltip_label.place_forget()
            self.tooltip_visible = False
