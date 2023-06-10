from src.functions import load_operation, conv_date, conv_number_account, conv_number_kart
from src.main import main
import sys


FILE = "package.json"

def test_main(capsys):
    operations = load_operation(FILE)
    main()
    captured = capsys.readouterr()
    assert "22.12.2018 Перевод с карты на карту" in captured.out









