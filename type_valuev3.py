import copy
from enum import Enum

from intbase import InterpreterBase


# Enumerated type for our different language data types
class Type(Enum):
    INT = 1
    BOOL = 2
    STRING = 3
    CLOSURE = 4
    NIL = 5
    OBJECT = 6

class Result(Enum):
    SUCCESS = 0
    FAILURE = 1


class Object:
    def __init__(self):
        self.dict = {}

    def get(self, field):
        d = self.dict
        while d is not None:
            if field in d:
                return d[field]

            if "proto" in d and d["proto"].type() != Type.NIL:
                p_value = d["proto"]
                p_obj = p_value.value()
                d = p_obj.dict
            else:
                d = None

        return None

    def set(self, field, val):
        if field == "proto" and val.type() not in (Type.OBJECT, Type.NIL):
            return Result.FAILURE
        self.dict[field] = val
        return Result.SUCCESS

    def __str__(self):
        return str(self.dict)


class Closure:
    def __init__(self, func_ast, env):
        self.captured_env = copy.deepcopy(env)
        self.func_ast = func_ast
        self.type = Type.CLOSURE


# Represents a value, which has a type and its value
class Value:
    def __init__(self, t, v=None):
        self.t = t
        self.v = v

    def value(self):
        return self.v

    def type(self):
        return self.t

    def set(self, other):
        self.t = other.t
        self.v = other.v


def create_value(val):
    if val == InterpreterBase.TRUE_DEF:
        return Value(Type.BOOL, True)
    elif val == InterpreterBase.FALSE_DEF:
        return Value(Type.BOOL, False)
    elif isinstance(val, int):
        return Value(Type.INT, val)
    elif val == InterpreterBase.NIL_DEF:
        return Value(Type.NIL, None)
    elif isinstance(val, str):
        return Value(Type.STRING, val)


def get_printable(val):
    if val.type() == Type.INT:
        return str(val.value())
    if val.type() == Type.STRING:
        return val.value()
    if val.type() == Type.BOOL:
        if val.value() is True:
            return "true"
        return "false"
    return None
