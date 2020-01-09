#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import dateutil.parser
from datetime import datetime, timezone


def _add_default_tz(x, tzinfo):
    return x.replace(tzinfo=x.tzinfo or tzinfo)


def convert_toms_str(s):
    digits_only = re.compile(r"\d+")
    if digits_only.fullmatch(s):
        dt = datetime.utcfromtimestamp(int(s) / 1000) \
            .replace(microsecond=int(s[-3:]) * 1000) \
            .replace(tzinfo=timezone.utc)
        return dt.isoformat()
    else:
        date = dateutil.parser.isoparse(s)
        date = _add_default_tz(date, timezone.utc)
        return str(int(date.timestamp() * 1000.0))
