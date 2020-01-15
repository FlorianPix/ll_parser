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
    # sema = Sema(ast)
    # ok = sema.check()

    # pretty print the AST
    print(str(ast))

    # print("Scoping OK:" + str(ok))


if __name__ == '__main__':
    main()
