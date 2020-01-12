#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import dateutil.parser
from datetime import datetime
from dateutil import tz
from calendar import timegm


def iso_to_millis(s):
    date = dateutil.parser.isoparse(s)
    return str(date_to_millis(date))


def date_to_millis(d):
    return str(int((timegm(d.timetuple()) + d.microsecond / 1000000.0) * 1000))


def millis_to_iso(millis):
    dt = datetime.utcfromtimestamp(int(millis) / 1000) \
        .replace(microsecond=int(millis[-3:]) * 1000) \
        .replace(tzinfo=tz.tzutc())
    return dt.isoformat()


def convert_toms_str(s):
    digits_only = re.compile(r"(?:\d+$)")
    if digits_only.match(s):
        return millis_to_iso(s)
    else:
        return iso_to_millis(s)
