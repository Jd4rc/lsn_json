import json
from pathlib import Path
from src.utils.decorators import log



BASE_DIR = Path(__file__).resolve().parent.parent.parent

@log
def filter_finance_transaction(datas, currency=None):

    with open(BASE_DIR / 'data' / datas) as f:
        transactions = json.load(f)

    if currency:
        filtered_data = list(filter(lambda x: x["currency"] == currency, transactions))
    else:
        filtered_data = transactions

    with open(BASE_DIR / 'data' / 'transactions_output.json', 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

    return filtered_data