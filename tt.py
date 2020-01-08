#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import dateutil.parser
from datetime import datetime, timezone


def add_default_tz(x, tzinfo):
    return x.replace(tzinfo=x.tzinfo or tzinfo)


if __name__ == '__main__':

    args = sys.argv[1:]
    digits_only = re.compile(r"\d+")
    for arg in args:
        if digits_only.fullmatch(arg):
            dt = datetime.utcfromtimestamp(int(arg) / 1000) \
                .replace(microsecond=int(arg[-3:]) * 1000) \
                .replace(tzinfo=timezone.utc)
            print(dt.isoformat())
        else:
            date = dateutil.parser.parse(arg)
            date = add_default_tz(date, timezone.utc)
            print(int(date.timestamp() * 1000.0))
