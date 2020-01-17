# toms - unix timestamp converter

[ ![PyPI](https://img.shields.io/pypi/v/toms)](https://pypi.org/project/toms/)

toms is a command line tool that allows
 to convert unix epoch millis to UTC iso date. And back

## install

```pip3 install toms --upgrade```

## examples

```
toms 1500000000000
2017-07-14T02:40:00+00:00
```

```
toms 2017-07-14T02:40
1500000000000
```

```
echo '2019-01-01 2020-01-01T10:12' | toms
1546300800000
1577873520000
```
