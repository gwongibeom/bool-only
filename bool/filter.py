import locale

locale.setlocale(locale.LC_ALL, '')


def format_datetime(value, fmt='%Y/%m/%d'):
    return value.strftime(fmt)
