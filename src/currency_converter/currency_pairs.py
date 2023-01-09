class CurrencyPair:
    def __init__(
        self,
        name: str,
        rate: float,
        display_name: str = None,
        display_currency_from_value="",
        display_currency_to_value="",
    ):
        self.name = name
        self.exchange_rate: float = rate
        if not display_name:
            display_name = str(self)
        self.display_name = display_name
        self.display_currency_from_value = display_currency_from_value
        self.display_currency_to_value = display_currency_to_value

    def to_currency(self, value) -> float:
        return value * self.exchange_rate

    def from_currency(self, value) -> float:
        # TODO FIXME: Fix the reverse calculation
        return value


class ChfEur(CurrencyPair):
    def __init__(self):
        name = "chf_eur"
        rate: float = 1.0153
        display_name: str = "CHF / EUR"
        super().__init__(
            name,
            rate,
            display_name,
            display_currency_from_value="CHF",
            display_currency_to_value="EUR",
        )


class ChfUsd(CurrencyPair):
    """TODO: Implement CHF / USD currency pair"""

    pass


## TODO: Add an additional currency pair of your choice
