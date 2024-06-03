from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Muhibz is smelly</h1>"

wbawdauwb

