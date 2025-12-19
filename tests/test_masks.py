from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("5555666677778888") == "55556******88"
    assert get_mask_card_number("7000792289606361") == "70007******61"
    assert get_mask_card_number("1111222233334444") == "11112******44"
    assert get_mask_card_number("9999888877776666") == "99998******66"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("11111111111111111111") == "**1111"
    assert get_mask_account("98765432109876543210") == "**3210"
    assert get_mask_account("00000000000000000000") == "**0000"
    assert get_mask_account("12345678901234567890") == "**7890"
