from toms import toms


def test_to_millis():
    assert toms.convert_toms_str('1970-01-01T00:00:00+00:00') == '0'


def test_to_iso_date():
    assert toms.convert_toms_str('0') == '1970-01-01T00:00:00+00:00'
