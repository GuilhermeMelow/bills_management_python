from uuid import UUID
from flask import current_app

from src.Decorators.Auth import auth_requests
from src.Repositories.PersonRepository import FamilyRepository


def family_controller():
    app = current_app

    @auth_requests(app=app)
    def controller_wrapper():
        repository = FamilyRepository()

        @app.get("/family/<family_id>")
        def find(family_id):
            result = repository.find(UUID(family_id))

            return result
