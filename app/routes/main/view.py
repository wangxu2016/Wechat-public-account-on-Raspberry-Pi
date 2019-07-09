from . import bp
from flask import current_app
from app.models import weixin

@bp.route('/')
def show():
    print(current_app.config['SECRET'])
    return '{"ret":"this is main page"}'
