# toms - unix timestamp converter

[ ![PyPI](https://img.shields.io/pypi/v/toms)](https://pypi.org/project/toms/)

Features:
 * Convert unix epoch millis to UTC iso date
 * Convert UTC iso date to unix epoch millis
 * Read from stdin
 * Replace all occurrences of unix epoch millis with iso date in text
 * Print current time millis

## install

```pip3 install toms```

## examples

Convert unix epoch millis to UTC iso date

```
toms 1500000000000
2017-07-14T02:40:00+00:00
```

Convert UTC iso date to unix epoch millis

```
toms 2017-07-14T02:40
1500000000000
```

Read from stdin

```
echo '2019-01-01 2020-01-01T10:12' | toms
1546300800000
1577873520000
```

Replace all occurrences of unix epoch millis with iso date in text

```
echo 'text 1500000000000 text' > /tmp/some-text.txt
cat /tmp/some-text.txt | toms replace
text 2017-07-14T02:40:00+00:00 text
```

Print current time millis

```
toms now
1592335604695
```
