class Closure:
    def __init__(self, statements, captures):
        """Init statements and captures

        Args:
            statements ([Statement]): lambda's statements
            captures ([{ string:Value }]): captured environment
        """
        self.statements = statements
        self.captures = captures

    def get_captures(self):
        return self.captures

    def set_captures(self, new_captures):
        self.captures = new_captures

    def get_statements(self):
        return self.statements
