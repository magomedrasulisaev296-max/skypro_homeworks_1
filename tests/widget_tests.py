from src.widget import mask_account_card, get_date


def test_masks_and_dates():
    # mask_account_card тесты
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("счет 73654108430135874305") == "счет **4305"
    assert mask_account_card("Discover 60113770209626562022") == "Discover 6011 37** **** 2022"

    # get_date тесты
    assert get_date("2023-10-05T12:30:45") == "05.10.2023"
    assert get_date("2023-10-05") == "05.10.2023"
    assert get_date("invalid-date") == "invalid-date"
    assert get_date("") == ""
    assert get_date("2023-10") == "2023-10"