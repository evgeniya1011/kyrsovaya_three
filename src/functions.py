import json
from datetime import datetime

def load_operation(FILE):
    """
    Вывод последних 5-ти операций EXECUTED
    """
    with open(FILE, "r", encoding="utf -8") as file:
        result = json.load(file)
        result_executed = []
        for operation in result:
            try:
                if operation["state"] == "EXECUTED":
                    result_executed.append(operation)
            except LookupError:
                result_error = "Операция не выполнена"
        last_operations = result_executed[-5:]
        sorted_operations = sorted(last_operations,key=lambda x: x["date"], reverse=True)
        return sorted_operations


def conv_date(data):
    """
    Форматирование даты
    """
    thedate = datetime.fromisoformat(data)
    date_formatted = thedate.strftime("%d.%m.%Y")
    return date_formatted


def conv_number_kart(number_kart=""):
    """
    Форматирование номера карты
    """
    new = number_kart.split(" ")
    new_number = new[-1][:4] + " " + new[-1][4:6] + "**" + " " + "****" + " " + new[-1][-4:]
    new[-1] = new_number
    return " ".join(new)


def conv_number_account(number_account):
    """
    Форматирование номера счета
    """
    account = number_account.split(" ")
    new_account = "**" + account[-1][-4:]
    account[-1] = new_account
    return " ".join(account)
