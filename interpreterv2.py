from brewparse import parse_program
from env_v1 import EnvironmentManager
from intbase import ErrorType, InterpreterBase
from operations_v2 import setup_ops, setup_unary_ops
from type_valuev1 import Type, Value, create_value, get_printable


# Main interpreter class
class Interpreter(InterpreterBase):
    # constants
    NIL_VALUE = create_value(InterpreterBase.NIL_DEF)
    BIN_OPS = {"+", "-", "*", "/", "==", "<", "<=", ">", ">=", "!=", "&&", "||"}
    UNARY_OPS = {"neg", "!"}

    # methods
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)
        self.trace_output = trace_output
        self.op_to_lambda = setup_ops()
        self.unary_op_to_lambda = setup_unary_ops()
        self.block_id_counter = 0

    # run a program that's provided in a string
    # usese the provided Parser found in brewparse.py to parse the program
    # into an abstract syntax tree (ast)
    def run(self, program):
        ast = parse_program(program)
        self.__set_up_function_table(ast)
        main_func = self.__get_func_by_name("main")
        self.env = EnvironmentManager(self.trace_output)
        self.__run_statements(main_func.get("statements"))

    def __set_up_function_table(self, ast):
        self.func_name_to_ast = {}
        for func_def in ast.get("functions"):
            if func_def.get("name") not in self.func_name_to_ast:
                self.func_name_to_ast[func_def.get("name")] = {}
            self.func_name_to_ast[func_def.get("name")][
                len(func_def.get("args"))
            ] = func_def
        if self.trace_output:
            print(self.func_name_to_ast)

    def __get_func_by_name(self, name, num_args=0):
        if name not in self.func_name_to_ast:
            super().error(ErrorType.NAME_ERROR, f"Function {name} not found")
        if num_args not in self.func_name_to_ast[name]:
            super().error(
                ErrorType.NAME_ERROR, f"Function {name} with {num_args} args not found"
            )
        return self.func_name_to_ast[name][num_args]

    def __run_statements(self, statements):
        """Execute a block of statements then clean up variables about to go out of scope upon finishing

        Args:
            statements ([Statement]): Iterable of statements representing a Block

        Returns:
            Any: return value if the Block is a function. This value is meaningless for other Blocks.
        """
        block_id = self.__unique_block_id()
        self.env.init_block_env(block_id)

        for statement in statements:
            # if self.trace_output:
            #     print(statement)
            if statement.elem_type == InterpreterBase.FCALL_DEF:
                self.__call_func(statement)
            elif statement.elem_type == "=":
                self.__assign(statement, block_id)
            # new statement types
            elif statement.elem_type == InterpreterBase.IF_DEF:
                self.__handle_if_statement(statement)
            elif statement.elem_type == InterpreterBase.WHILE_DEF:
                self.__handle_while_statement(statement)
            elif statement.elem_type == InterpreterBase.RETURN_DEF:
                return self.__handle_return_statement(statement)

        return self.__destroy_block_and_return(block_id, Interpreter.NIL_VALUE)

    def __call_func(self, call_node):
        func_name = call_node.get("name")
        if func_name == "print":
            return self.__call_print(call_node)
        if func_name == "inputi" or func_name == "inputs":
            return self.__call_input(call_node)

        func = self.__get_func_by_name(
            func_name, len(call_node.get("args"))
        )  # includes NAME_ERROR check

        # block_id = self.__unique_block_id()
        # self.env.init_block_env(block_id)
        # add params to top scope and initialize them to the evaluations of the corresponding args

        self.__run_statements(func.get("statements"))

        # clean up the args




    def __call_print(self, call_ast):
        output = ""
        for arg in call_ast.get("args"):
            result = self.__eval_expr(arg)  # result is a Value object
            output = output + get_printable(result)
        super().output(output)
        return Interpreter.NIL_VALUE

    def __call_input(self, call_ast):
        args = call_ast.get("args")
        if args is not None and len(args) == 1:
            result = self.__eval_expr(args[0])
            super().output(get_printable(result))
        elif args is not None and len(args) > 1:
            super().error(
                ErrorType.NAME_ERROR, "No input function that takes > 1 parameter"
            )
        inp = super().get_input()
        if call_ast.get("name") == "inputi":
            return Value(Type.INT, int(inp))
        if call_ast.get("name") == "inputs":
            return Value(Type.STRING, inp)

    def __assign(self, assign_ast, block_id):
        var_name = assign_ast.get("name")
        value_obj = self.__eval_expr(assign_ast.get("expression"))
        self.env.set(var_name, value_obj, block_id)

    def __handle_if_statement(self, statement):
        condition = self.__eval_expr(statement.get("condition"))
        if condition.type() is not Type.BOOL:
            super().error(
                ErrorType.TYPE_ERROR,
                f"Condition type in if is {condition.type()}, expected Type.BOOL",
            )
        if condition.value():
            self.__run_statements(statement.get("statements"))
        elif statement.get("else_statements") is not None:
            self.__run_statements(statement.get("else_statements"))

    def __handle_while_statement(self, statement):
        condition = self.__eval_expr(statement.get("condition"))
        if condition.type() is not Type.BOOL:
            super().error(
                ErrorType.TYPE_ERROR,
                f"Condition type in while is {condition.type()}, expected Type.BOOL",
            )
        while condition.value():
            self.__run_statements(statement.get("statements"))
            condition = self.__eval_expr(statement.get("condition"))
            if condition.type() is not Type.BOOL:
                super().error(
                    ErrorType.TYPE_ERROR,
                    f"Condition type in while is {condition.type()}, expected Type.BOOL",
                )

    def __handle_return_statement(self, statement):
        unevaluated_expr = statement.get("expression")
        if unevaluated_expr is None:
            return Interpreter.NIL_VALUE
        return self.__eval_expr(unevaluated_expr)

    def __eval_expr(self, expr_ast):
        if expr_ast.elem_type == InterpreterBase.INT_DEF:
            return Value(Type.INT, expr_ast.get("val"))
        if expr_ast.elem_type == InterpreterBase.STRING_DEF:
            return Value(Type.STRING, expr_ast.get("val"))
        if expr_ast.elem_type == InterpreterBase.BOOL_DEF:
            return Value(Type.BOOL, expr_ast.get("val"))
        if expr_ast.elem_type == InterpreterBase.NIL_DEF:
            return Interpreter.NIL_VALUE
        if expr_ast.elem_type == InterpreterBase.VAR_DEF:
            var_name = expr_ast.get("name")
            val = self.env.get(var_name)
            if val is None:
                super().error(ErrorType.NAME_ERROR, f"Variable {var_name} not found")
            return val
        if expr_ast.elem_type == InterpreterBase.FCALL_DEF:
            return self.__call_func(expr_ast)
        if expr_ast.elem_type in Interpreter.BIN_OPS:
            return self.__eval_op(expr_ast)
        if expr_ast.elem_type in Interpreter.UNARY_OPS:
            return self.__eval_unary_op(expr_ast)

    def __eval_op(self, arith_ast):
        left_value_obj = self.__eval_expr(arith_ast.get("op1"))
        right_value_obj = self.__eval_expr(arith_ast.get("op2"))
        if left_value_obj.type() != right_value_obj.type():
            super().error(
                ErrorType.TYPE_ERROR,
                f"Incompatible types for {arith_ast.elem_type} operation (different types)",
            )
        if arith_ast.elem_type not in self.op_to_lambda[left_value_obj.type()]:
            super().error(
                ErrorType.TYPE_ERROR,
                f"Incompatible operator {arith_ast.elem_type} for type {left_value_obj.type()}",
            )
        f = self.op_to_lambda[left_value_obj.type()][arith_ast.elem_type]
        return f(left_value_obj, right_value_obj)

    def __eval_unary_op(self, arith_ast):
        value_obj = self.__eval_expr(arith_ast.get("op1"))
        if arith_ast.elem_type not in self.unary_op_to_lambda[value_obj.type()]:
            super().error(
                ErrorType.TYPE_ERROR,
                f"Incompatible operator {arith_ast.elem_type} for type {value_obj.type()}",
            )
        f = self.unary_op_to_lambda[value_obj.type()][arith_ast.elem_type]
        return f(value_obj)

    def __unique_block_id(self):
        self.block_id_counter = self.block_id_counter + 1
        return self.block_id_counter

    def __destroy_block_and_return(self, block_id, ret):
        self.env.destroy_block_env(block_id)
        return ret

    # def __link_args_to_params(self, args, params, block_id):
    #     for a, p in zip(args, params):
    #         self.env.set(p, a, block_id)