from ricetypes import Option, Result


class A:
    def __init__(self, x):
        self.x = x

    def method_1(self, y):
        return A(x=self.x + y)

    def method_2(self, y):
        x = self.x + y
        self.x = x
        return x


def test_1():
    assert Option.Some(A(1)).map(A.method_1, 10).value.x == 11
    assert not Option.Nothing.map(A.method_1, 10).something


def test_2():
    assert Result.Ok(A(1)).map(A.method_1, 10).unwrap().x == 11
    e = Result.Error(A(1)).map(A.method_1, 10).maperr(A.method_1, 100)
    assert e.error
    assert e.get_error().value.x == 101


def test_3():
    op = Option.Some(A(1))
    op.do(A.method_2, 10)
    assert op.value.x == 11


def test_4():
    r = Result.Ok(A(1))
    r.do(A.method_2, 10).doerr(A.method_2, 100)
    assert not r.error
    assert r.unwrap().x == 11

    r = Result.Error(A(1))
    r.do(A.method_2, 10).doerr(A.method_2, 100)
    assert r.error
    assert r.get_error().value.x == 101
