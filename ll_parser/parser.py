# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink


from . import ast


class Parser:
    """Parser for arithmetic expressions

    Args:
       tokens (List[str]): List of all tokens

    Attributes:
       current_token (str): The token currently being processed
       remaining_tokens (List[str]): List of unprocessed tokens
    """

    def __init__(self, tokens):
        self.current_token = None
        self.remaining_tokens = tokens

    def consume_token(self):
        """Consume a token and return it

        Remove the next token from ``remaining_tokens`` and update
        ``current_token``.

        Returns:
            str: The current token
        """
        if len(self.remaining_tokens) > 0:
            self.current_token = self.remaining_tokens.pop(0)
        else:
            self.current_token = None
        return self.current_token

    def accept_token(self, expected):
        """Consume a token and verify

        Verify that the current token is the ``expected`` token, remove the
        next token from ``remaining_tokens`` and update ``current_token``.

        Args:
            expected (str): Expected token

        Returns:
            str: The current token

        Raises:
            RuntimeError: if the ``current_token`` is not the ``expected`` token
        """
        t = self.current_token
        if t is None:
            raise RuntimeError('Expected token %s but found end of stream' %
                               expected)
        if t.type != expected:
            raise RuntimeError('Expected token %s but found %s' % (expected,
                                                                   t.type))
        return self.consume_token()

    def parseS(self):
        """Parse non-terminal S"""
        self.consume_token()  # read the first token
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing S (end of stream)')

        if (t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'
                or t.type == 'LET'):
            result = self.parseE()
            # we should have processed all tokens by now
            if self.current_token is not None:
                raise RuntimeError('Error while parsing S (did not reach end '
                                   'of stream, current token: %s' %
                                   self.current_token)
            return result
        else:
            raise RuntimeError('Error while parsing S (current token %s)' % t)

    def parseE(self):
        """Parse non-terminal E"""
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing E (end of stream)')

        if (t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'):
            left = self.parseT()
            return self.parseEp(left)
        elif t.type == 'LET':
            t = self.consume_token()
            name = t.value
            self.accept_token('IDENTIFIER')
            self.accept_token('EQUALS')
            init = self.parseE()
            self.accept_token('IN')
            return ast.Let(name, init, self.parseE())
        else:
            raise RuntimeError('Error while parsing E (current token %s)' % t)

    def parseT(self):
        """Parse non-terminal T"""
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing T (end of stream)')

        if(t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'):
            left = self.parseF()
            return self.parseTp(left)
        else:
            raise RuntimeError('Error while parsing T (current token %s)' % t)

    def parseF(self):
        """Parse non-terminal F"""
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing F (end of stream)')

        if t.type == 'LPARAN':
            self.consume_token()
            result = self.parseE()
            self.accept_token('RPARAN')
            return result
        elif t.type == 'INT_LIT':
            self.consume_token()
            return ast.IntLit(t.value)
        elif t.type == 'FLOAT_LIT':
            self.consume_token()
            return ast.FloatLit(t.value)
        elif t.type == 'IDENTIFIER':
            self.consume_token()
            return ast.Identifier(t.value)
        else:
            raise RuntimeError('Error while parsing F (current token %s)' % t)

    def parseTp(self, left):
        """Parse non-terminal Tp"""
        t = self.current_token

        if (t is None
                or t.type == 'PLUS'
                or t.type == 'RPARAN'
                or t.type == 'IN'):
            return left
        elif t.type == 'STAR':
            self.consume_token()
            right = self.parseF()
            left = ast.BinOp('MUL', left, right)
            return self.parseTp(left)
        else:
            raise RuntimeError("Error while parsing Tp' (current token %s)" % t)

    def parseEp(self, left):
        """Parse non-terminal Ep"""
        t = self.current_token

        if (t is None
                or t.type == 'RPARAN'
                or t.type == 'IN'):
            return left
        elif t.type == 'PLUS':
            self.consume_token()
            right = self.parseT()
            left = ast.BinOp('ADD', left, right)
            return self.parseEp(left)
        else:
            raise RuntimeError("Error while parsing Ep' (current token %s)" % t)
