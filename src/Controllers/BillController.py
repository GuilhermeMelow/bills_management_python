from flask import Flask, json, Response

from src.Repositories.BillRepository import BillRepository


def bill_controller(app: Flask):
    repository = BillRepository()

    @app.get("/bills")
    def list_bills():
        bills = repository.list()

        return Response(json.dumps(bills))
