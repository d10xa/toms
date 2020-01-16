#!/usr/bin/env python3
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


def convert_toms_str(s: str) -> str:
    if _regex_digits_only.match(s):
        return millis_to_iso(s)
    else:
        return iso_to_millis(s)
