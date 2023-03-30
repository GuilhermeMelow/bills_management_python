
from uuid import UUID
from dateutil.parser import parse
from flask import Request, current_app, jsonify, request, make_response

from src.Controllers.Bill.BillResponse import BillResponse
from src.Decorators.Auth import auth_requests
from src.Models.Bill import Bill
from src.Repositories.BillRepository import BillRepository


def bill_controller():
    app = current_app

    @auth_requests(app=app)
    def controller_wrapper():
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
            bill = __map_bill(request)

            repository.add(bill)
            result = BillResponse.create(bill)

            return make_response(jsonify(result), 201)

        @app.put("/bills/<bill_id>")
        def bills_update(bill_id):
            bill = __map_bill(request, bill_id)

            repository.update(UUID(bill_id), bill)
            result = BillResponse.create(bill)

            return make_response((jsonify(result)), 201)

        def __map_bill(request: Request, bill_id=None):
            dct: dict[str, str] = request.get_json()

            return Bill(description=dct["description"],
                        due_date=parse(dct["due_date"]),
                        price=float(dct["price"]),
                        id=bill_id)

    controller_wrapper()
