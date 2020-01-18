#! /usr/bin/python3
# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink

import sys

from .lexer import lexer
from .parser import Parser
from .sema import Sema


def main():
    # read input
    lexer.input(sys.stdin.read())

    # Tokenize
    tokens = list(lexer)

    # parse and create AST
    parser = Parser(tokens)
    ast = parser.parseS()

    # perform semantic analysis
    sema = Sema(ast)
    ok, type = sema.check()

    # pretty print the AST
    print(str(ast))

    print("Scoping OK: " + str(ok) + "\nType: " + str_type(type))


def str_type(type):
    if type == 2:
        return "FLOAT"
    elif type == 1:
        return "INT"
    else:
        return "ERR"


if __name__ == '__main__':
    main()
