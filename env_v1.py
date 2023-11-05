# The EnvironmentManager class keeps a mapping between each variable (aka symbol)
# in a brewin program and the value of that variable - the value that's passed in can be
# anything you like. In our implementation we pass in a Value object which holds a type
# and a value (e.g., Int, 10).
class EnvironmentManager:
    def __init__(self, trace_output):
        self.environment = {}
        self.trace_output = trace_output

    def init_block_env(self, block_id):
        self.environment[block_id] = {}

    # Gets the data associated a variable name
    def get(self, symbol):
        """Return the value corresponding to symbol at the highest possible scope. Return None if no such symbol is alive.

        Args:
            symbol (string): name of the variable

        Returns:
            Any: value of variable or None if no variable corresponding to symbol is alive
        """
        for block_env in self.environment.values():
            # if self.trace_output:
            #     print("Looking through block: ", block_env)
            if symbol in block_env:
                return block_env[symbol]
        return None

    # Sets the data associated with a variable name
    def set(self, symbol, value, block_id):
        """Sets the data associated with a variable name

        Args:
            symbol (string): Variable name
            value (Value): Value object mapped to by the name
        """
        # Check if the symbol is already defined and in scope.
        for block_env in self.environment.values():
            if symbol in block_env:
                block_env[symbol] = value
                return
        # If not, instantiate a new variable.
        self.environment[block_id][symbol] = value

    def destroy_block_env(self, block_id):
        del self.environment[block_id]
