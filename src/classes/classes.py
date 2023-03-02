"""BozoGenerator functionality"""


class BozoGenerator:
    """The BozoGenerator provides very bs example generators"""

    def __init__(self):
        self._default_generator = BozoGenerator.create_generator()

    def default_generator(self):
        return self._default_generator

    @staticmethod
    def generator():
        """Generate a sequence of two  numbers"""
        yield 1
        yield 2
        yield 3

    @staticmethod
    def create_generator():
        return (x for x in range(1, 10))

    def re_init(self):
        """re initialize our default generator"""
        self._default_generator = BozoGenerator.create_generator()


if __name__ == '__main__':
    for index, value in enumerate(BozoGenerator.generator()):
        print(f'index: {index}, value: {value}')

    bg = BozoGenerator()

    print(list(bg.default_generator()))
    print(list(bg.default_generator()))
    bg.re_init()
    print(list(bg.default_generator()))
