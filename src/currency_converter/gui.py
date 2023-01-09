import sys
from tkinter import *
from tkinter.ttk import Combobox

from currency_converter.converter import ChfEur, ChfUsd, CurrencyConverter


class CurrencyConverterGuiApp:
    DIRECTION_FROM_TO = ">>"
    DIRECTION_TO_FROM = "<<"

    def __init__(self, currency_converter: CurrencyConverter = None):
        if not currency_converter:
            # TODO: Add the ChfUsd currency pair
            currency_converter = CurrencyConverter([ChfEur()])
        self.currency_converter = currency_converter
        self.window = Tk()
        self.window.title("Currency Converter")
        self.container = Frame(self.window)
        self.container.pack()
        self._init_all()

    def _init_all(self):
        self.direction = self.DIRECTION_FROM_TO
        self._init_combobox()
        self._init_labels()
        self._init_entry_boxes()
        self._init_buttons()

    def _init_combobox(self):
        values = []
        for key, pair in self.currency_converter.registered_pairs.items():
            values.append(pair.display_name)
        self.combo_box = Combobox(self.container, values=values)
        self.combo_box.configure(state="readonly")
        self.combo_box.pack()
        self.combo_box.bind("<<ComboboxSelected>>", self.switch_currency_pair)
        self.combo_box.current(0)

    def _init_labels(self):
        self.label_exchange_rate = Label()
        self.label_exchange_rate.pack(side=RIGHT)
        self.__label_set_exchange_rate()

    def __label_set_exchange_rate(self):
        self.label_exchange_rate.configure(
            text=f"Exchange rate: {self.currency_converter.get_exchange_rate()}"
        )

    def _init_entry_boxes(self):
        self.entry_from_value = Entry(self.container)
        self.entry_to_value = Entry(self.container)
        self.entry_from_value.pack(side=LEFT)
        self.entry_to_value.pack(side=RIGHT)

    def _init_buttons(self):
        self.btn_toogle_direction = Button(self.container)
        self.btn_toogle_direction.configure(text=">>")
        self.btn_toogle_direction.pack()
        self.btn_toogle_direction.bind("<Button-1>", self.toggle_direction)

        self.btn_calculate = Button(self.container)
        self.btn_calculate.configure(text="Calculate")
        self.btn_calculate.pack()
        self.btn_calculate.bind("<Button-1>", self.calculate)

    def _calculate_from_to(self):
        value = self.entry_from_value.get()
        to_value = self.currency_converter.to_currency(float(value))
        self.entry_to_value.delete(0, last=END)
        self.entry_to_value.insert(0, str(to_value))

    def _calculate_to_from(self):
        value = self.entry_to_value.get()
        from_value = self.currency_converter.from_currency(float(value))
        self.entry_from_value.delete(0, last=END)
        self.entry_from_value.insert(0, str(from_value))

    def calculate(self, event):
        if self.direction == self.DIRECTION_FROM_TO:
            self._calculate_from_to()
        elif self.direction == self.DIRECTION_TO_FROM:
            self._calculate_to_from()

    def toggle_direction(self, event):
        direction = event.widget.cget("text")
        if direction == "<<":
            direction = ">>"
        else:
            direction = "<<"
        event.widget.configure(text=direction)
        self.direction = direction

    def switch_currency_pair(self, event):
        selected_display_name = event.widget.get()
        pair_key_name = self.currency_converter.get_currency_pair_key_from(
            selected_display_name
        )
        self.currency_converter.set_selected_pair(pair_key_name)
        self.__label_set_exchange_rate()


def main():
    app = CurrencyConverterGuiApp()
    app.window.iconify()
    app.window.update()
    app.window.deiconify()
    return app.window.mainloop()


if __name__ == "__main__":
    sys.exit(main())
