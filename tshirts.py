
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(37.9) == 'S')
assert(size(38.1) == 'S')
assert(size(37.9) == 'M')
assert(size(38.1) == 'M')
assert(size(41.9) == 'M')
assert(size(42.1) == 'M')
assert(size(43) == 'L')
assert(size(42.1) == 'L')
print("All is well (maybe!)\n")
