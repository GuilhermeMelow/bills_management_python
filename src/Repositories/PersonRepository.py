from src.Models.User import Person
from src.Repositories.Repository import Repository


class PersonRepository(Repository[Person, Person]):
    def __init__(self):
        super().__init__("person")
