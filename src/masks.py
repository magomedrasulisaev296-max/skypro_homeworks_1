def get_mask_card_number(card_number: str) -> str:
    """функция принимает номер карты и шифрует числа находяшийися по центру"""

    masked_card_number = card_number.replace(card_number[5:14], "******")

    return masked_card_number
print(get_mask_card_number("5555666677778888"))#55556******88
print(get_mask_card_number("7000792289606361"))
print(get_mask_card_number("1111222233334444"))
print(get_mask_card_number("9999888877776666"))



def get_mask_account(account_number: str) -> str:
    """Функция принимает номер аккаунта и скрывает первые его две цифры"""
    if len(account_number) == 20:
        replaced_account_number = account_number.replace(account_number[0:-4], "**")
        return replaced_account_number
print(get_mask_account("73654108430135874305"))#4305
