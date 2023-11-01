from type_valuev1 import Type, Value


def setup_ops():
    """Generate BINARY ops lambdas"""
    op_to_lambda = {}
    # set up operations on integers
    op_to_lambda[Type.INT] = {}
    op_to_lambda[Type.INT]["+"] = lambda x, y: Value(x.type(), x.value() + y.value())
    op_to_lambda[Type.INT]["-"] = lambda x, y: Value(x.type(), x.value() - y.value())
    # add other operators here later for int, string, bool, etc
    # rest of int ops
    op_to_lambda[Type.INT]["*"] = lambda x, y: Value(x.type(), x.value() * y.value())
    op_to_lambda[Type.INT]["/"] = lambda x, y: Value(x.type(), x.value() // y.value())
    op_to_lambda[Type.INT]["<"] = lambda x, y: Value(Type.BOOL, x.value() < y.value())
    op_to_lambda[Type.INT]["<="] = lambda x, y: Value(Type.BOOL, x.value() <= y.value())
    op_to_lambda[Type.INT][">"] = lambda x, y: Value(Type.BOOL, x.value() > y.value())
    op_to_lambda[Type.INT][">="] = lambda x, y: Value(Type.BOOL, x.value() >= y.value())
    op_to_lambda[Type.INT]["=="] = lambda x, y: Value(Type.BOOL, x.value() == y.value())
    op_to_lambda[Type.INT]["!="] = lambda x, y: Value(Type.BOOL, x.value() != y.value())
    # string
    op_to_lambda[Type.STRING] = {}
    op_to_lambda[Type.STRING]["+"] = lambda x, y: Value(x.type(), x.value() + y.value())
    op_to_lambda[Type.STRING]["=="] = lambda x, y: Value(
        Type.BOOL, x.value() == y.value()
    )
    op_to_lambda[Type.STRING]["!="] = lambda x, y: Value(
        Type.BOOL, x.value() != y.value()
    )
    # bool
    op_to_lambda[Type.BOOL] = {}
    op_to_lambda[Type.BOOL]["=="] = lambda x, y: Value(
        Type.BOOL, x.value() == y.value()
    )
    op_to_lambda[Type.BOOL]["!="] = lambda x, y: Value(
        Type.BOOL, x.value() != y.value()
    )
    op_to_lambda[Type.BOOL]["&&"] = lambda x, y: Value(Type.BOOL, x.value() & y.value())
    op_to_lambda[Type.BOOL]["||"] = lambda x, y: Value(Type.BOOL, x.value() | y.value())

    return op_to_lambda


def setup_unary_ops():
    unary_op_to_lambda = {}
    # int
    unary_op_to_lambda[Type.INT] = {}
    unary_op_to_lambda[Type.INT]["neg"] = lambda x: Value(
        x.type(), -(x.value())
    )
    # bool
    unary_op_to_lambda[Type.BOOL] = {}
    unary_op_to_lambda[Type.BOOL]["!"] = lambda x: Value(
        x.type(), not x.value()
    )

    return unary_op_to_lambda
