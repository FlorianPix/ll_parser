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
            return True, 1
        elif isinstance(node, ast.FloatLit):
            return True, 2
        else:
            raise RuntimeError('unexpected AST node')

    def check_binop(self, node):
        assert isinstance(node, ast.BinOp)
        ok_1, type_1 = self.check_node(node.left)
        ok_2, type_2 = self.check_node(node.right)
        return ok_1 and ok_2, max(type_1, type_2)

    def check_let(self, node):
        assert isinstance(node, ast.Let)
        ok_1, type_1 = self.check_node(node.init)
        self.sym_tab.append((node.name, type_1))
        ok_2, type_2 = self.check_node(node.expr)
        self.sym_tab.pop()
        return ok_1 and ok_2, type_2

    def check_identifier(self, node):
        assert isinstance(node, ast.Identifier)
        for sym in self.sym_tab:
            if sym[0] == node.name:
                return True, sym[1]
        print("ERROR: variable '%s' not in scope" % node.name)
        return False, 0
