import sys

digits = {
    "one": "1",
    "two" : "2",
    "three" : "3"
}


def convert(tokens: list[str]):

    try:
        number = ''

        for token in tokens:
            number += digits[token]

        return int(number)
    except (KeyError, TypeError) as e:
        print(f'error: {e!r}', file=sys.stderr)
        raise

