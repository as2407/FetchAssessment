import math
import re
import uuid

from models.receipt import Receipt
from datetime import datetime, time

database = {}


def evaluate_point(receipt: Receipt):
    point = 0
    alpha_numeric_pattern = r'^[a-zA-Z0-9]+$'
    for c in receipt.retailer.lower():
        if re.match(alpha_numeric_pattern, c) is not None:
            point += 1

    total = float(receipt.total)
    if total.is_integer():
        point += 50

    if total % 0.25 == 0:
        point += 25

    point += (len(receipt.items) // 2) * 5

    for item in receipt.items:
        if len(item.short_description.strip()) % 3 == 0:
            value = float(item.price) * 0.2
            point += math.ceil(value)

    date_object = datetime.strptime(receipt.purchase_date, "%Y-%m-%d")
    if date_object.day % 2 != 0:
        point += 6

    purchase_time = datetime.strptime(receipt.purchase_time, "%H:%M").time()
    if time(14, 0) < purchase_time < time(16, 0):
        point += 10

    random_uuid = str(uuid.uuid4())
    database[random_uuid] = point
    return random_uuid


def get_point(receipt_id: str):
    return database.get(receipt_id)
