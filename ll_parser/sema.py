# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink


from . import ast


class Sema:

    def __init__(self, ast):
        self.ast = ast
        self.sym_tab = []

    def check(self):
        return self.check_node(self.ast)

    def check_node(self, node):
        if isinstance(node, ast.Let):
            return self.check_let(node)
        elif isinstance(node, ast.Identifier):
            return self.check_identifier(node)
        elif isinstance(node, ast.BinOp):
            return self.check_binop(node)
        elif isinstance(node, ast.IntLit):
            return True
        elif isinstance(node, ast.FloatLit):
            return True
        else:
            raise RuntimeError('unexpected AST node')

    def check_binop(self, node):
        assert isinstance(node, ast.BinOp)
        ok_1 = self.check_node(node.left)
        ok_2 = self.check_node(node.right)
        return ok_1 and ok_2

    def check_let(self, node):
        assert isinstance(node, ast.Let)
        ok_1 = self.check_node(node.init)
        self.sym_tab.append(node.name)
        ok_2 = self.check_node(node.expr)
        self.sym_tab.pop()
        return ok_1 and ok_2

    def check_identifier(self, node):
        assert isinstance(node, ast.Identifier)
        for sym in self.sym_tab:
            if sym == node.name:
                return True
        return False
