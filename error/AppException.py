#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from .APIException import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(APIException):
    code = 202
    msg = 'delete ok'
    error_code = 1


class UpdateSuccess(APIException):
    code = 200
    msg = 'update ok'
    error_code = 2


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake!'
    error_code = 999


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'


class RuntimeException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)

