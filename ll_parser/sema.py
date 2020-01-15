# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink


from . import ast


class Sema:

    def __init__(self, ast):
        self.ast = ast

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
        raise NotImplementedError('check_binop is not yet implemented!')

    def check_let(self, node):
        assert isinstance(node, ast.Let)
        raise NotImplementedError('check_let is not yet implemented!')

    def check_identifier(self, node):
        assert isinstance(node, ast.Identifier)
        raise NotImplementedError('check_identifier is not yet implemented!')
