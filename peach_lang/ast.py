class Program:
    """
    The main program node. This node has all of the program expressions as children
    :var expressions: The expressions our Program consists of.
    """
    def __init__(self, expressions):
        """
        Creates a new program node
        :param expressions: The expression children our program node has
        """
        self.expressions = expressions

    def __str__(self):
        return "\n".join(str(expr) for expr in self.expressions)

    # TODO: Nicer printing
    def __repr__(self):
        return "Program(\n{}\n)".format(
            ",\n".join(repr(expr) for expr in self.expressions))

class Expression:
    """
    The base expression class. Our current calculator is made up a list of Expressions.
    """

class Literal(Expression):
    """
    A node to represent an atomic expression within our program

    :var value: The value of this class
    """
    def __init__(self, value):
        """
        Creates a new Literal node
        :param value: The value of our literal
        """
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Literal({})".format(repr(self.value))

class BinaryExpression(Expression):
    """
    The base class to represent any expression involving two numbers
    """

    def __init__(self, left, right):
        """
        Creates a new Binary Expression node
    :   param left: The left operand
    :   param right: The right operand
        """
        self.left = left
        self.right = right


class Add(BinaryExpression):
    """
    A node to represent the addition of two numbers
    """

    def __str__(self):
        return "{} + {}".format(str(self.left), str(self.right))

    def __repr__(self):
        return "Add({}, {})".format(repr(self.left), repr(self.right))


class Sub(BinaryExpression):
    """
    A node to represent the subtraction of two numbers
    """

    def __str__(self):
        return "{} - {}".format(str(self.left), str(self.right))

    def __repr__(self):
        return "Sub({}, {})".format(repr(self.left), repr(self.right))

class Mult(BinaryExpression):
    """
    A node to represent the multiplication of two numbers
    """

    def __str__(self):
        return "{} * {}".format(str(self.left), str(self.right))

    def __repr__(self):
        return "Mult({}, {})".format(repr(self.left), repr(self.right))


class Div(BinaryExpression):
    """
    A node to represent the division of two numbers
    """

    def __str__(self):
        return "{} / {}".format(str(self.left), str(self.right))

    def __repr__(self):
        return "Div({}, {})".format(repr(self.left), repr(self.right))