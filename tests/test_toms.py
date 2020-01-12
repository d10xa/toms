from toms import toms


def test_to_millis():
    assert toms.convert_toms_str('1970-01-01T00:00:00+00:00') == '0'
    assert toms.convert_toms_str(
        '2017-12-01T10:12:03.123000+00:00') == '1512123123123'


def test_to_iso_date():
    assert toms.convert_toms_str('0') == '1970-01-01T00:00:00+00:00'
    assert toms.convert_toms_str(
        '1512123123123') == '2017-12-01T10:12:03.123000+00:00'
