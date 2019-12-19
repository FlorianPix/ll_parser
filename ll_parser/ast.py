# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink


"""AST module

This module contains multiple classes that each represent an AST
node. Furthermore, it defines the function ``indent(s, n)`` as a helper for
pretty printing.
"""


import textwrap


def indent(s, n):
    """Add indentation to multiline string

    Args:
       s (str): Input string
       n (int): Number of indentation spaces

    Returns:
        str: ``s`` indented by ``n`` spaces
    """
    return textwrap.indent(s, n*' ')


class IntLit:
    """Integer literal AST node

    Args:
       value (int): Value of the integer literal

    Attributes:
       value (int): Value of the integer literal
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        """Convert to string (pretty print)"""
        return 'INTEGER LIT. <%d>\n' % (self.value)


class FloatLit:
    """Float literal AST node

    Args:
       value (float): Value of the float literal

    Attributes:
       value (float): Value of the float literal
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        """Convert to string (pretty print)"""
        return 'FLOAT LIT. <%f>\n' % (self.value)


class Identifier:
    """Identifier AST node

    Args:
       name (str): Name of the identifier

    Attributes:
       name (str): Name of the identifier
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """Convert to string (pretty print)"""
        return 'IDENTIFIER <%s>\n' % (self.name)


class BinOp:
    """Binary Operator AST node

    Args:
       kind (str): Name of the operation ('MUL' or 'ADD')
       left: AST node left to the operator
       right: AST node right to the operator

    Attributes:
       name (str): Name of the identifier
       left: AST node left to the operator
       right: AST node right to the operator
    """

    def __init__(self, kind, left, right):
        self.kind = kind
        self.left = left
        self.right = right

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'BINARY OP. <%s>\n' % (self.kind)
        result += indent(str(self.left), 2)
        result += indent(str(self.right), 2)
        return result