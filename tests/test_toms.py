from toms import convert_toms_str
from toms import replace_millis_str


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
    assert convert_toms_str('1969-12-31T23:59:58.001+00:00') == '-1999'
    assert convert_toms_str('1969-12-31T23:59:58.555+00:00') == '-1445'
    assert convert_toms_str('-1445') == '1969-12-31T23:59:58.555000+00:00'


def test_minus_small_millis():
    assert convert_toms_str('1969-12-31T23:59:59.999+00:00') == '-1'
    assert convert_toms_str('-1') == '1969-12-31T23:59:59.999000+00:00'


def test_replace_millis():
    assert replace_millis_str(
        'abc1000000000000def') == 'abc2001-09-09T01:46:40+00:00def'
    assert replace_millis_str(
        '0000000000000 asdfjlasfj 9999999999999') == \
        '1970-01-01T00:00:00+00:00 asdfjlasfj' \
        ' 2286-11-20T17:46:39.999000+00:00'
