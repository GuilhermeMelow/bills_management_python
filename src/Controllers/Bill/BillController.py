
from uuid import UUID

from flask import Flask, jsonify, request, make_response

from src.Controllers.Bill.BillRequest import BillRequest
from src.Controllers.Bill.BillResponse import BillResponse
from src.Models.Bill import Bill
from src.Repositories.BillRepository import BillRepository


def bill_controller(app: Flask):
    repository = BillRepository()

    @app.get("/bills")
    def bills_list():
        bills = repository.list()
        result = jsonify([BillResponse.create(bill) for bill in bills])

        return make_response(result, 200)

    @app.get("/bills/<bill_id>")
    def bills_find(bill_id):
        bill = repository.find(UUID(bill_id))

        return make_response(BillResponse.create(bill), 200)

    @app.post("/bills")
    def bills_register():
        bill_request = BillRequest.create(request.get_json())
        bill = __map_bill(bill_request)

        repository.add(bill)
        result = BillResponse.create(bill)

        return make_response(jsonify(result), 201)

    @app.put("/bills/<bill_id>")
    def bills_update(bill_id):
        bill_request = BillRequest.create(request.get_json(), bill_id)
        bill = __map_bill(bill_request)

        repository.update(UUID(bill_id), bill)
        result = BillResponse.create(bill)

        return make_response((jsonify(result)), 201)

    def __map_bill(bill_request: BillRequest):
        return Bill(description=bill_request.description,
                    due_date=bill_request.due_date,
                    price=bill_request.price,
                    id=bill_request.id)
