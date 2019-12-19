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
        self.consume_token()  # read the first token
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing S (end of stream)')

        if (t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'):
            print(self.parseE(None, None)[0])
            # we should have processed all tokens by now
            if self.current_token is not None:
                raise RuntimeError('Error while parsing S (did not reach end '
                                   'of stream, current token: %s' %
                                   self.current_token)
        else:
            raise RuntimeError('Error while parsing S (current token %s)' % t)

    def parseE(self, val, left):
        """Parse non-terminal E"""
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing E (end of stream)')

        if (t.type == 'LPARAN'
                or t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'):
            val = self.parseEp(None, self.parseT(None, None)[0])[0]
            return val, None
        raise RuntimeError('Error while parsing E (current token %s)' % t)

    def parseT(self, val, left):
        """Parse non-terminal T"""
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing T (end of stream)')

        if (t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'
                or t.type == 'IDENTIFIER'
                or t.type == 'LPARAN'):
            val = self.parseTp(None, self.parseF(None, None)[0])[0]
            return val, None
        raise RuntimeError('Error while parsing T (current token %s)' % t)

    def parseF(self, val, left):
        """Parse non-terminal F"""
        t = self.current_token

        if t is None:
            raise RuntimeError('Error while parsing F (end of stream)')

        if (t.type == 'INT_LIT'
                or t.type == 'FLOAT_LIT'):
            self.consume_token()
            return t.value, None
        elif t.type == 'IDENTIFIER':
            self.consume_token()
            return None, None
        elif t.type == 'LPARAN':
            self.consume_token()
            val = self.parseE(None, None)[0]
            self.accept_token('RPARAN')
            return val, None
        raise RuntimeError('Error while parsing F (current token %s)' % t)

    def parseTp(self, val, left):
        """Parse non-terminal Tp"""
        t = self.current_token
        if (t is None
                or t.type == 'PLUS'
                or t.type == 'RPARAN'):
        elif t.type == 'STAR':
            self.consume_token()
            val = self.parseTp(None, left * self.parseF(None, None)[0])[0]
            return val, None
        raise RuntimeError('Error while parsing Tp (current token %s)' % t)

    def parseEp(self, val, left):
        """Parse non-terminal Ep"""
        t = self.current_token

        if (t is None
                or t.type == 'RPARAN'):
            val = left
            return val, left
        elif t.type == 'PLUS':
            self.consume_token()
            val = self.parseEp(None, left + self.parseT(None, None)[0])[0]
            return val, None

        raise RuntimeError('Error while parsing Ep (current token %s)' % t)
