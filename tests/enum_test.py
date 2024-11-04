from ricetypes import Enum, Scalar_Variant, Struct_Variant


def test_enum_construct():
    @Enum
    class Color:
        Red:   Scalar_Variant
        Blue:  Scalar_Variant = 10
        Green: Scalar_Variant = 'g'
        Magenta: Scalar_Variant = 13, 'mag'

        RGB: Struct_Variant(int, int, int)
        HSL: Struct_Variant(H=float, S=float, L=float)

    r = Color.Red
    b = Color.Blue
    g = Color.Green
    m = Color.Magenta

    assert r is not b
    assert r is Color.Red
    assert Color.RGB(255, 255, 255).tuple == (255, 255, 255)
    assert Color.HSL(.5, .5, .5).H == .5
    assert str(r) == 'Red'
    assert int(r) == 0
    assert int(b) == 10
    assert int(g) == 11
    assert int(m) == 13
    assert str(m) == 'mag'


def issue_No4_test():
    @Enum
    class A:
        v1: Scalar_Variant
        v2: Scalar_Variant = 2
        v3: Scalar_Variant = 'variant 3'
        v4: Scalar_Variant = 'variant 4', 40
        v5: Scalar_Variant = 50, 'variant 5'

    assert int(A.v1) == 0
    assert str(A.v1) == 'v1'

    assert int(A.v2) == 2
    assert str(A.v2) == 'v2'

    assert int(A.v3) == 3
    assert str(A.v3) == 'variant 3'

    assert int(A.v4) == 40
    assert str(A.v4) == 'variant 4'

    assert int(A.v5) == 50
    assert str(A.v5) == 'variant 5'
