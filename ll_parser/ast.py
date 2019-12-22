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
    """

    def __init__(self, value):
        self.kind = 'INTLIT'
        self.value = value

    def __str__(self):
        """Convert to string (pretty print)"""
        return 'INTEGER LIT. <%d>\n' % self.value


class FloatLit:
    """Float literal AST node

    Args:
        value (float): Value of the float literal
    """

    def __init__(self, value):
        self.kind = 'FLOATLIT'
        self.value = value

    def __str__(self):
        """Convert to string (pretty print)"""
        return 'FLOAT LIT. <%f>\n' % self.value


class Identifier:
    """Identifier AST node

    Args:
        name (str): Name of the identifier
    """

    def __init__(self, name):
        self.kind = 'IDENTIFIER'
        self.name = name

    def __str__(self):
        """Convert to string (pretty print)"""
        return 'IDENTIFIER <%s>\n' % self.name


class PLUS:
    """Identifier AST node"""

    def __init__(self):
        self.kind = '+'

    def __str__(self):
        """Convert to string (pretty print)"""
        return '%s\n' % self.kind


class STAR:
    """Identifier AST node"""

    def __init__(self):
        self.kind = '*'

    def __str__(self):
        """Convert to string (pretty print)"""
        return '%s\n' % self.kind


class EPSILON:
    """Identifier AST node"""

    def __init__(self):
        self.kind = 'EPSILON'

    def __str__(self):
        """Convert to string (pretty print)"""
        return '%s\n' % self.kind


class LPARAN:
    """Identifier AST node"""

    def __init__(self):
        self.kind = '('

    def __str__(self):
        """Convert to string (pretty print)"""
        return '%s\n' % self.kind


class RPARAN:
    """Identifier AST node"""

    def __init__(self):
        self.kind = ')'

    def __str__(self):
        """Convert to string (pretty print)"""
        return '%s\n' % self.kind


class DOLLAR:
    """Identifier AST node"""

    def __init__(self):
        self.kind = '$'

    def __str__(self):
        """Convert to string (pretty print)"""
        return '%s\n' % self.kind


class S:
    """Binary Operator AST node
    Args:
       children: child nodes
    """

    def __init__(self, children):
        self.kind = 'S'
        self.children = children

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'S.\n'
        for child in self.children:
            result += indent(str(child), 2)
        return result


class E:
    """Binary Operator AST node
    Args:
       children: child nodes
    """

    def __init__(self, children):
        self.kind = 'E'
        self.children = children

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'E.\n'
        for child in self.children:
            result += indent(str(child), 2)
        return result


class T:
    """Binary Operator AST node
    Args:
       children: child nodes
    """

    def __init__(self, children):
        self.kind = 'T'
        self.children = children

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'T.\n'
        for child in self.children:
            result += indent(str(child), 2)
        return result


class F:
    """Binary Operator AST node
    Args:
        children: child nodes
    """

    def __init__(self, children):
        self.kind = 'F'
        self.children = children

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'F.\n'
        for child in self.children:
            result += indent(str(child), 2)
        return result


class Tp:
    """Binary Operator AST node
    Args:
       children: child nodes
    """

    def __init__(self, children):
        self.kind = 'Tp'
        self.children = children

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'Tp.\n'
        for child in self.children:
            result += indent(str(child), 2)
        return result


class Ep:
    """Binary Operator AST node
    Args:
       children: child nodes
    """

    def __init__(self, children):
        self.kind = 'Ep'
        self.children = children

    def __str__(self):
        """Convert to string (pretty print)"""
        result = 'Ep.\n'
        for child in self.children:
            result += indent(str(child), 2)
        return result
