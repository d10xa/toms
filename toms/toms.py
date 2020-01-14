#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import dateutil.parser
from datetime import datetime, timezone


def iso_to_millis(s):
    date = dateutil.parser.isoparse(s)
    return str(date_to_millis(date))


def _add_default_tz(x, tzinfo):
    return x.replace(tzinfo=x.tzinfo or tzinfo)


def date_to_millis(date):
    date = _add_default_tz(date, timezone.utc)
    return int(date.timestamp() * 1000.0)


def millis_to_iso(millis):
    dt = datetime.utcfromtimestamp(int(millis) / 1000) \
        .replace(microsecond=int(millis[-3:]) * 1000) \
        .replace(tzinfo=timezone.utc)
    return dt.isoformat()


def convert_toms_str(s):
    digits_only = re.compile(r"(?:-?\d+$)")
    if digits_only.match(s):
        return millis_to_iso(s)
    else:
        return iso_to_millis(s)
