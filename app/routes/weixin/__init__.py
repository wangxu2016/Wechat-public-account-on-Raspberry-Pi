from flask import Blueprint

bp = Blueprint('weixin', __name__)
from . import view