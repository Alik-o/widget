from src.widget import mask_account_card

with open("number_card.txt", encoding="utf-8") as file:
    numbers_card = file.read()
    numbers_card_list = numbers_card.split("\n")
    for num in numbers_card_list:
        print(mask_account_card(num))
