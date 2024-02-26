import re


def validate_data(data: dict) -> bool:
    keys = data.keys()
    if 'shortDescription' not in keys or 'price' not in keys:
        return False

    short_description = data.get('shortDescription')
    price = data.get('price')

    return re.match("^[\\w\\s\\-]+$", short_description) is not None and re.match("^\\d+\\.\\d{2}$", price) is not None


class Item:
    def __init__(self, short_description, price):
        self.short_description: str = short_description
        self.price: str = price
