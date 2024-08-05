import os

from config import DATA_DIR
from src.filter import search_by_description
from src.processing import filter_by_state, sort_by_date
from src.utils import get_amount_transaction_rubles, get_financial_transaction_data
from src.widget import get_data, mask_account_card

filtering_status = ["EXECUTED", "CANCELED", "PENDING"]
file_transaction = {1: "operations.json", 2: "transactions.csv", 3: "transactions_excel.xlsx"}

print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

while True:
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    while True:
        user_input_file = input()
        if user_input_file == "1":
            print("Для обработки выбран JSON-файл.")
            break
        elif user_input_file == "2":
            print("Для обработки выбран CSV-файл.")
            break
        elif user_input_file == "3":
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Введено некорректное значение. Попробуйте еще раз.")

    data_transaction = get_financial_transaction_data(os.path.join(DATA_DIR, file_transaction[int(user_input_file)]))

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        user_input_status = input()
        if user_input_status.upper() in filtering_status:
            print(f"Операции отфильтрованы по статусу {user_input_status.upper()}.")
            break
        else:
            print(f"Статус операции {user_input_status} недоступен.")

    data_transaction_filtered = filter_by_state(data_transaction, user_input_status.upper())

    print("Отсортировать операции по дате? Да/Нет")
    user_input_sort = input().lower()

    if user_input_sort == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_sort_order = input().lower()
        if user_input_sort_order == "по возрастанию":
            print("Операции отсортированы по возрастанию даты.")
            data_transaction_sorted = sort_by_date(data_transaction_filtered, ascending=True)
        else:
            print("Операции отсортированы по убыванию даты.")
            data_transaction_sorted = sort_by_date(data_transaction_filtered, ascending=False)
    else:
        data_transaction_sorted = data_transaction_filtered

    print("Выводить только рублевые транзакции? Да/Нет")
    user_input_currency = input().lower()

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input_search = input().lower()

    if user_input_search == "да":
        print("Введите слово для поиска.")
        user_input_search_string = input()
        data_transaction_search = search_by_description(data_transaction_sorted, user_input_search_string)
    else:
        data_transaction_search = data_transaction_sorted

    print("Распечатываю итоговый список транзакций...\n")

    print(f"Всего банковских операций в выборке: {len(data_transaction_search)}\n")
    for transaction in data_transaction_search:
        print(f"{get_data(transaction['date'])} {transaction['description']}")
        if transaction.get("from"):
            print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
        else:
            print(f'{mask_account_card(transaction["to"])}')
        if user_input_currency == "да":
            if user_input_file == "1":
                print(
                    f'Сумма: {get_amount_transaction_rubles(transaction)}руб.\n'
                )
            else:
                print(f'Сумма: {get_amount_transaction_rubles(transaction)}руб.\n')
        else:
            if user_input_file == "1":
                print(
                    f'Сумма: {transaction["operationAmount"]["amount"]} '
                    f'{transaction["operationAmount"]["currency"]["name"]}\n'
                )
            else:
                print(f'Сумма: {transaction["amount"]} {transaction["currency_name"]}\n')
    print("Продолжить работу с банковскими транзакциями? Да/Нет")
    continue_working = input().lower()
    if continue_working == "нет":
        break
