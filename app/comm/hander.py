#!/usr/bin/python  
# -*-coding:utf-8-*-
import functools
from flask import request, jsonify, abort


def require(*required_args):
    def decorator(func):
        @functools.wraps(func)
        def warps(*args, **kwargs):
            for arg in required_args:
                if arg not in request.form:
                    return abort(400)
            return func(*args, **kwargs)
        return warps
    return decorator
