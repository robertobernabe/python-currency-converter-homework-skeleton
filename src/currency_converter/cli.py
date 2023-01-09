import argparse
import sys

from .converter import CurrencyConverter
from .currency_pairs import ChfEur, ChfUsd


def create_parser(currency_options: list[str]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cli interface to the currency converter"
    )
    parser.add_argument("value", type=float, help="Numerical value.")
    parser.add_argument("currency_pair", choices=currency_options, help="")
    parser.add_argument("--reverse", action="store_true", help="")
    return parser


def run_currency_converter(
    currency_converter: CurrencyConverter, value: float, pair_name: str, reverse=False
):
    currency_converter.set_selected_pair(pair_name)
    if not reverse:
        result = currency_converter.to_currency(value)
    else:
        result = currency_converter.from_currency(value)
    print(result)


def main():
    # TODO: Add the ChfUsd currency pair
    cc = CurrencyConverter([ChfEur()])
    parser = create_parser(cc.registered_pairs.keys())
    args = parser.parse_args()
    run_currency_converter(cc, args.value, args.currency_pair, reverse=args.reverse)


if __name__ == "__main__":
    sys.exit(main())
