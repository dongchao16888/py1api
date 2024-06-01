#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from flask import Blueprint

room_blueprint = Blueprint('room_blueprint', __name__)


from . import action