# Copyright 2017 TU Dresden
# All rights reserved.
#
# Authors: Christian Menard
#          Norman Rink


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
        print("S")
        self.consume_token()  # read the first token
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing S (end of stream)')

        if (t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'):
            print(self.parseE()[1])
            # we should have processed all tokens by now
            if self.current_token is not None:
                raise RuntimeError('Error while parsing S (did not reach end '
                                   'of stream, current token: %s' %
                                   self.current_token)
            print('Parsing was successful')
        else:
            raise RuntimeError('Error while parsing S (current token %s)' % t)

    def parseE(self):
        """Parse non-terminal E"""
        print("E")
        t = self.current_token
        if (t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'):
            val = self.parseT()[1]
            fun = self.parseEp()[0]
            if fun is None:
                return None, val
            return None, fun(val)
        raise RuntimeError('Error while parsing E (current token %s)' % t)

    def parseT(self):
        """Parse non-terminal T"""
        print("T")
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing T (end of stream)')

        if (t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'
                or t.type == 'LPARAN'):
            val = self.parseF()[1]
            fun = self.parseTp()[0]
            if fun is None:
                return None, val
            return None, fun(val)
        raise RuntimeError('Error while parsing T (current token %s)' % t)

    def parseF(self):
        """Parse non-terminal F"""
        print("F")
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing F (end of stream)')

        if t.type == 'INT_LIT':
            self.accept_token('INT_LIT')
            return None, t.value
        elif t.type == 'FLOAT_LIT':
            self.accept_token('FLOAT_LIT')
            return None, t.value
        elif t.type == 'IDENTIFIER':
            self.accept_token('IDENTIFIER')
            return None, None
        elif t.type == 'LPARAN':
            self.accept_token('LPARAN')
            val = self.parseE()[1]
            self.accept_token('RPARAN')
            return None, val
        raise RuntimeError('Error while parsing F (current token %s)' % t)

    def parseTp(self):
        """Parse non-terminal Tp"""
        print("Tp")
        t = self.current_token

        if t is None:
            return None, None
        elif t.type == 'PLUS':
            return None, None
        elif t.type == 'RPARAN':
            return None, None
        elif t.type == 'STAR':
            self.accept_token('STAR')
            val = self.parseF()[1]
            fun = self.parseTp()[0]
            if fun is None:
                def bun(ar):
                    return ar * val
            else:
                def bun(ar):
                    return fun(ar * val)
            return bun, None
        raise RuntimeError('Error while parsing Tp (current token %s)' % t)

    def parseEp(self):
        """Parse non-terminal Ep"""
        print("Ep")
        t = self.current_token

        if t is None:
            return None, None
        elif t.type == 'RPARAN':
            return None, None
        elif t.type == 'PLUS':
            self.accept_token('PLUS')
            val = self.parseT()[1]
            fun = self.parseEp()[0]
            if fun is None:
                def bun(ar):
                    return ar + val
            else:
                def bun(ar):
                    return fun(ar + val)
            return bun, None

        raise RuntimeError('Error while parsing Ep (current token %s)' % t)
