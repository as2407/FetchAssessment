from flask import Flask, request, jsonify
from models import receipt
from service import evaluation_service

app = Flask(__name__)


@app.post('/receipts/process')
def process_receipts():
    data = request.get_json()
    if not receipt.validate_data(data):
        return jsonify({"error": "The receipt is invalid"}), 400

    receipt_obj = receipt.Receipt(
        data.get('retailer'), data.get('purchaseDate'),
        data.get('purchaseTime'), data.get('items'),
        data.get('total')
    )

    evaluation_id = evaluation_service.evaluate_point(receipt_obj)
    return jsonify({"id": evaluation_id}), 200


@app.get('/receipts/<receipt_id>/points')
def get_points(receipt_id):
    point = evaluation_service.get_point(receipt_id)
    if point is None:
        return jsonify({"error": "No receipt found with that ID"}), 404

    return jsonify({"points": point}), 200


if __name__ == '__main__':
    app.run()
