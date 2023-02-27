from flask import Flask

from src.Controllers.BillController import bill_controller

app = Flask(__name__)


@app.get("/")
def testing_default():
    return "Everything is fine, there is no worries now :)"


bill_controller(app)
