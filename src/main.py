from functions import load_operation, conv_date, conv_number_account, conv_number_kart

FILE = "operations.json"


def main():
    """
    Вывод отформатированных 5-ти последних операций
    """
    operations = load_operation(FILE)
    for operation in operations:
        operation["date"] = conv_date(operation["date"])
        try:
            if "Счет" in operation["from"]:
                operation["from"] = conv_number_account(operation["from"])
            else:
                operation["from"] = conv_number_kart(operation["from"])
        except LookupError:
            operation["from"] = "Неизвестный источник"

        if "Счет" in operation["to"]:
            operation["to"] = conv_number_account(operation["to"])
        else:
            operation["to"] = conv_number_kart(operation["to"])
        print(operation["date"] + " " + operation["description"])
        print(operation["from"] + "->" + operation["to"])
        print(operation["operationAmount"]["amount"] + " " + operation["operationAmount"]["currency"]["name"], end="\n  \n")


if __name__ == "__main__":
    main()
