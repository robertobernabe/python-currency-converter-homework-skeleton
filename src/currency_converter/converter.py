from .currency_pairs import ChfEur, ChfUsd, CurrencyPair


class CurrencyConverter:
    DEFAULT = "default"

    def __init__(self, currency_pairs: list[CurrencyPair]):
        self.pairs = {}
        self.pairs[self.DEFAULT] = currency_pairs[0].name
        for pair in currency_pairs:
            self.pairs[pair.name] = pair
        self.selected = self.DEFAULT

    def register(self, currency_pair: CurrencyPair):
        self.pairs[currency_pair.name] = currency_pair

    @property
    def default_pair(self) -> CurrencyPair:
        default_key = self.pairs.get(self.DEFAULT)
        return self.pairs.get(default_key)

    @property
    def registered_pairs(self) -> dict:
        _ = {k: v for k, v in self.pairs.items() if k != "default"}
        return _

    @property
    def selected_pair(self) -> CurrencyPair:
        if self.selected == self.DEFAULT:
            self.selected = self.pairs.get(self.selected, None)
        pair = self.pairs.get(self.selected)
        return pair

    def set_selected_pair(self, pair_name: str):
        if pair_name in self.registered_pairs.keys():
            self.selected = pair_name
        else:
            print(f"Didn't found key name {pair_name}")

    def to_currency(self, value: float) -> float:
        print(f"From {self.selected_pair.display_currency_from_value} to {self.selected_pair.display_currency_to_value}")
        return round(self.selected_pair.to_currency(value), 2)

    def from_currency(self, value: float) -> float:
        print(f"From {self.selected_pair.display_currency_to_value} to {self.selected_pair.display_currency_from_value}")
        return round(self.selected_pair.from_currency(value), 2)

    def get_exchange_rate(self) -> float:
        return self.selected_pair.exchange_rate

    def get_currency_pair_key_from(self, display_name: str) -> str or None:
        for key, pair in self.registered_pairs.items():
            if pair.display_name.lower() == display_name.lower().strip():
                return key
