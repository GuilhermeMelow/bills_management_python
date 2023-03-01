import json
from uuid import UUID

from dateutil.parser import parse
from flask import Flask, jsonify, request, make_response

from src.Controllers.Bill.BillResponse import BillResponse
from src.Models.Bill import Bill
from src.Repositories.BillRepository import BillRepository


def bill_controller(app: Flask):
    repository = BillRepository()

    @app.get("/bills")
    def list_bills():
        bills = repository.list()

        return make_response(jsonify([BillResponse.create(bill) for bill in bills]), 200)

    @app.route("/bills/<bill_id>")
    def find(bill_id):
        bill = repository.find(UUID(bill_id))

        return make_response(BillResponse.create(bill), 200)

    @app.post("/bills")
    def register():
        bill: Bill = json.loads(request.data, object_hook=__as_bill_request)

        repository.add(bill)

        return jsonify(BillResponse.create(bill))

    def __as_bill_request(dct: [str, str]) -> Bill:
        return Bill(description=dct["description"],
                    price=dct["price"],
                    due_date=parse(dct["due_date"]))
