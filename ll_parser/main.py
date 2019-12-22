#! /usr/bin/python3
# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink

import sys

from .lexer import lexer
from .parser import Parser
from .visual import vis


def main():
    # read input
    lexer.input(sys.stdin.read())

    # Tokenize
    tokens = list(lexer)

    # parse and create AST
    parser = Parser(tokens)
    ast = parser.parseS()

    # really pretty print ast with latex
    vis(ast)


if __name__ == '__main__':
    main()
