DELAY = '~d'
TAB = '~t'
ENTER = '~e'
SPACE = '\x20'


def textify(value: str) -> str:
    contents = [value, TAB]
    return ''.join([delayify(item) for item in contents if item is not None])


def listify(value: str) -> str:
    contents = [SPACE, value, ENTER, TAB]
    return ''.join([delayify(item) for item in contents])


def delayify(value: str, amount=1) -> str:
    delay_count = DELAY * amount
    return delay_count + value


def tabify(amount=1) -> str:
    tab_count = TAB * amount
    return tab_count
