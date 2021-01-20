def gen_letters(start, x):
    i = start
    end = start + x
    while i < end:
        yield chr(i)
        i += 1


def letters(upper):
    if upper:
        yield from gen_letters(65, 26)
    else:
        yield from gen_letters(97, 26)


for letter in letters(False):
    print(letter)


for letter in letters(True):
    print(letter)
