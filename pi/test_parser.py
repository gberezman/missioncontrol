from parser import Parser

class TestParser:

    def test_token_returnsNone_whenInputIsNone(self):
        parser = Parser(None)
        assert parser.token() is None

    def test_next_returnsNone_whenInputIsNone(self):
        parser = Parser(None)
        assert parser.next() is None

    def test_token_returnsInputToken(self):
        parser = Parser('a')
        assert parser.token() == 'a'

    def test_token_returnsNone_afterInputIsExhausted(self):
        parser = Parser('a')
        parser.next()
        assert parser.token() is None

    def test_next_returnsNone_afterInputIsExhausted(self):
        parser = Parser('a')
        assert parser.next() is None

    def test_token_returnsSecondToken_whenMultipleTokens(self):
        parser = Parser('aa bb cc')
        parser.next()
        assert parser.token() == 'bb'
