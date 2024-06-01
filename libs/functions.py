#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>

import uuid


def generate_id():
    return uuid.uuid4().__str__()

