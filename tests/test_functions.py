from src.functions import conv_date, conv_number_account, conv_number_kart, load_operation

FILE = "src/package.json"
def test_conv_date():
    assert conv_date("2018-12-22T05:10:49.857412") == "22.12.2018"
    assert conv_date("2020-11-29T05:10:49.857412") == "29.11.2020"
    assert conv_date("2019-12-07") == "07.12.2019"


def test_conv_number_account():
    assert conv_number_account("Счет 67667879435628279708") == "Счет **9708"
    assert conv_number_account("Счет 52136987521645879321") == "Счет **9321"
    assert conv_number_account("Счет 74698521387561578924") == "Счет **8924"


def test_conv_number_kart():
    assert conv_number_kart("Карта 2842878893689012") == "Карта 2842 87** **** 9012"
    assert conv_number_kart("МИР 4878656375033856") == "МИР 4878 65** **** 3856"
    assert conv_number_kart("MasterCard 1435442169918409") == "MasterCard 1435 44** **** 8409"


def test_load_operation():
    file_list = [
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967"
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497"
        },
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880"
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412"
        }
    ]
    assert load_operation(FILE) == file_list
