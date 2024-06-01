#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from flask import Blueprint

hello_blueprint = Blueprint('hello_blueprint', __name__)


from . import action