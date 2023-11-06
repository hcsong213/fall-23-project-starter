# The EnvironmentManager class keeps a mapping between each variable (aka symbol)
# in a brewin program and the value of that variable - the value that's passed in can be
# anything you like. In our implementation we pass in a Value object which holds a type
# and a value (e.g., Int, 10).
class EnvironmentManager:
    def __init__(self, trace_output):
        self.environment = [{}]
        self.trace_output = trace_output

    def init_block_env(self):  # push to stack
        self.environment.append({})

    # Gets the data associated a variable name
    def get(self, symbol):
        """Return the value corresponding to symbol at the highest possible scope. Return None if no such symbol is alive.

        Args:
            symbol (string): name of the variable

        Returns:
            Any: value of variable or None if no variable corresponding to symbol is alive
        """
        # Citation: The following code was generated using ChatGPT 3.5
        for scope in reversed(self.environment):
            if symbol in scope:
                return scope[symbol]
        return None
        # End of copied code

    # Sets the data associated with a variable name
    def set(self, symbol, value):
        for scope in reversed(self.environment):
            if symbol in scope:
                scope[symbol] = value
                return
        # Var with symbol as name doesn't exist yet
        self.set_at_top_scope(symbol, value)

    def set_at_top_scope(self, symbol, value):
        """Forcefully shadows any variable to redeclare that variable at top scope.

        Should only be used at the beginning of function calls with params or as a helper function
        in this class.

        Args:
            symbol (string): name of var
            value (Value): value of var
        """
        # Citation: The following code was generated using ChatGPT 3.5
        self.environment[-1][symbol] = value
        # End of copied code

    def destroy_block_env(self):
        # Citation: The following code was generated using ChatGPT 3.5
        self.environment.pop()
        # End of copied code
