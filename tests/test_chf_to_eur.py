import pytest

from currency_converter.converter import CurrencyConverter
from currency_converter.currency_pairs import ChfEur, ChfUsd


def test_currency_converter_chf_to_eur():
    chfEur = ChfEur()
    cc = CurrencyConverter([chfEur])
    eur = cc.to_currency(4000)
    chf = cc.from_currency(eur)
    assert chf == 4000
    
    pairs = cc.registered_pairs
    for pair_name, pair in pairs.items():
        assert pair_name == chfEur.name
        assert isinstance(pair, ChfEur)

    cc.set_selected_pair(chfEur.name)
    chf_eur_key_name = cc.get_currency_pair_key_from(chfEur.display_name)
    assert chf_eur_key_name == chfEur.name


def test_currency_converter_chf_usd():
    chfUsd = ChfUsd()
    chfEur = ChfEur()
    cc = CurrencyConverter([chfEur, chfUsd])
    cc.set_selected_pair(chfUsd.name)
    usd = cc.to_currency(4500.12)
    chf = cc.from_currency(usd)
    assert chf == 4500.12
