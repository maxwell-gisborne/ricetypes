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
