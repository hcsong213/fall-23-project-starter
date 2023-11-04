# The EnvironmentManager class keeps a mapping between each variable (aka symbol)
# in a brewin program and the value of that variable - the value that's passed in can be
# anything you like. In our implementation we pass in a Value object which holds a type
# and a value (e.g., Int, 10).
class EnvironmentManager:
    def __init__(self):
        self.environment = {}

    # Gets the data associated a variable name
    def get(self, symbol):
        if symbol in self.environment:
            return self.environment[symbol]
        return None

    # Sets the data associated with a variable name
    def set(self, symbol, value):
        """Sets the data associated with a variable name

        Args:
            symbol (string): Variable name
            value (Value): Value object mapped to by the name
        """
        self.environment[symbol] = value
