from flask import Flask, jsonify

from src.Controllers.Bill.BillResponse import BillResponse
from src.Repositories.BillRepository import BillRepository


def bill_controller(app: Flask):
    repository = BillRepository()

    @app.get("/bills")
    def list_bills():
        bills = repository.list()

        return jsonify([BillResponse.create(bill) for bill in bills])

    @app.post("/bills")
    def register_bill():
        bills = repository.list()

        return jsonify([BillResponse.create(bill) for bill in bills])
