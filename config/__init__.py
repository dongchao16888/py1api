#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


import os
from .Default import Default
from .Develop import Develop
from .Produce import Produce
from .Test import Test


class GetConfig:

    conf = {
        'develop': Develop,
        'produce': Produce,
        'test': Test,
        'default': Default
    }

    @classmethod
    def run(cls):
        mode = os.getenv('APP_MODE') or None
        if mode not in cls.conf:
            mode = 'default'
        return cls.conf.get(mode)

