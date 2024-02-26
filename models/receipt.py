from datetime import datetime
import re
from models import item


def validate_data(data: dict) -> bool:
    keys = data.keys()
    if 'retailer' not in keys or \
            'purchaseDate' not in keys or 'purchaseTime' not in keys or 'items' not in keys or 'total' not in keys:
        return False

    retailer = data.get('retailer')
    purchase_date = data.get('purchaseDate')
    purchase_time = data.get('purchaseTime')
    items = data.get('items')
    total = data.get('total')
    return re.match("^[\\w\\s\\-]+", retailer) is not None and re.match("^\\d+\\.\\d{2}$", total) is not None \
           and _is_valid_date(purchase_date) and _is_valid_time(purchase_time) and _validate_items(items)


def _validate_items(items: list) -> bool:
    if len(items) >= 1:
        for i in items:
            if not item.validate_data(i):
                return False

    return True


def _is_valid_date(date_string: str) -> bool:
    date_format = '%Y-%m-%d'
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError as e:
        print(e)
        return False


def _is_valid_time(time_string: str) -> bool:
    time_format = '%H:%M'
    try:
        datetime.strptime(time_string, time_format)
        return True
    except ValueError as e:
        print(e)
        return False


class Receipt:
    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.retailer: str = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = [item.Item(i.get('shortDescription'), i.get('price')) for i in items]
        self.total = total

