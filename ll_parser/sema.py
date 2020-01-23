# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink


from . import ast


class Sema:
    ERROR = 0
    INTEGER = 1
    FLOAT = 2

    def __init__(self, ast):
        self.ast = ast
        self.symtab = []
        self.error = False

    def check(self):
        self.check_node(self.ast)
        return self.error

    def check_node(self, node):
        if isinstance(node, ast.Let):
            return self.check_let(node)
        elif isinstance(node, ast.Identifier):
            return self.check_identifier(node)
        elif isinstance(node, ast.BinOp):
            return self.check_binop(node)
        elif isinstance(node, ast.IntLit):
            return Sema.INTEGER
        elif isinstance(node, ast.FloatLit):
            return Sema.FLOAT
        else:
            raise RuntimeError('unexpected AST node')

    def check_binop(self, node):
        assert isinstance(node, ast.BinOp)
        return max(self.check_node(node.left), self.check_node(node.right))

    def check_let(self, node):
        assert isinstance(node, ast.Let)
        type = self.check_node(node.init)
        self.symtab_push(node.name, type)
        type = self.check_node(node.expr)
        self.symtab_pop()
        return type

    def check_identifier(self, node):
        assert isinstance(node, ast.Identifier)
        type = self.symbol_lookup(node.name)
        if type is Sema.ERROR:
            self.error = True
            print("ERROR: variable '%s' not in scope" % node.name)
            return Sema.ERROR
        return type

    def symtab_push(self, name, type):
        self.symtab.append((name, type))

    def symtab_pop(self):
        self.symtab.pop()

    def symbol_lookup(self, name):
        for n, t in reversed(self.symtab):
            if n == name:
                return t
        return Sema.ERROR
