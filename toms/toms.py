# -*- coding: utf-8 -*-

import re
from typing import Tuple

import dateutil.parser
from datetime import datetime, timedelta, timezone

_regex_digits_only = re.compile(r"(?:-?\d+$)")


def iso_to_millis(s):
    date = dateutil.parser.isoparse(s)
    return str(date_to_millis(date))


def _add_default_tz(x, tzinfo):
    return x.replace(tzinfo=x.tzinfo or tzinfo)


def date_to_millis(date):
    date = _add_default_tz(date, timezone.utc)
    return int(date.timestamp() * 1000.0)


def split_timestamp(s: str) -> Tuple[int, int, int]:
    sign = -1 if s.startswith('-') else 1
    if sign < 0:
        s = s[1:]
    ms = s[-3:]
    sec = s[0:-len(ms)]
    return sign, int(sec or '0'), int(ms or '0')


def millis_to_iso(s):
    (minus_sign, sec, ms) = split_timestamp(s)
    return make_iso(minus_sign, sec, ms)


def make_iso(sign: int, seconds: int, millis: int):
    delta = timedelta(milliseconds=millis * sign)
    dt = datetime.utcfromtimestamp(seconds * sign)
    dt = dt + delta
    dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat()


def replace_millis_str(s: str) -> str:
    # min with leading zeroes 0000000000000 1970-01-01T00:00:00+00:00
    # min 1000000000000 2001-09-09T01:46:40+00:00
    # max 9999999999999 2286-11-20T17:46:39.999000+00:00
    pattern = re.compile(r'\d+')
    items = re.findall(pattern, s)
    for i in items:
        j = str(i)
        if len(j) == 13:
            s = s.replace(i, millis_to_iso(j))
    return s


def convert_toms_str(s: str) -> str:
    if _regex_digits_only.match(s):
        return millis_to_iso(s)
    else:
        return iso_to_millis(s)
