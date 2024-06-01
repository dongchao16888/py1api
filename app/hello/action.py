#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from . import hello_blueprint


@hello_blueprint.route('/default', methods=['GET'])
def default():
    return 'hello world.'
