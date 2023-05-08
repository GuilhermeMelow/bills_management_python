

from uuid import UUID, uuid4
from flask import current_app, make_response, request

from src.Decorators.Auth import auth_requests
from src.Models.User import Person
from src.Repositories.PersonRepository import PersonRepository


def person_controller():
    app = current_app

    @auth_requests(app=app)
    def controller_wrapper():
        repository = PersonRepository()

        @app.get("/user/<person_id>")
        def find(person_id):
            person = repository.find(UUID(person_id))

            return make_response(person.__dict__, 200)

        @app.post("/user")
        def register():
            raw: dict[str, str] = request.get_json()

            if (raw.get("family_id") is None):
                # We should redirect user to family register endpoint.
                print("no family")

            person = __map_person(raw)

            repository.add(person)

            return make_response(person.__dict__, 201)

        @app.put("/user/<person_id>")
        def update(person_id):
            person = __map_person(request.get_json())

            repository.update(person_id, person)

            return make_response(person.__dict__, 201)

        def __map_person(raw: dict[str, str], person_id=None):
            return Person(**raw, id=person_id)

    controller_wrapper()
