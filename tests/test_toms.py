from toms import convert_toms_str


def test_to_millis():
    assert convert_toms_str('1970-01-01T00:00:00+00:00') == '0'
    assert convert_toms_str(
        '2017-12-01T10:12:03.123000+00:00') == '1512123123123'


def test_to_iso_date():
    assert convert_toms_str('0') == '1970-01-01T00:00:00+00:00'
    assert convert_toms_str(
        '1512123123123') == '2017-12-01T10:12:03.123000+00:00'


def test_timezone_plus():
    assert convert_toms_str('1970-01-01T04:00:00+03:00') == str(60 * 60 * 1000)


def test_timezone_minus():
    assert convert_toms_str('1970-01-01T04:00:00-03:00') == str(
        7 * 60 * 60 * 1000)


def test_negative_timestamp():
    assert convert_toms_str('1960-01-01T04:00:00-03:00') == '-315594000000'
    assert convert_toms_str('-315594000000') == '1960-01-01T07:00:00+00:00'
