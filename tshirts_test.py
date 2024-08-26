from tshirts import size
def test_size(cms):
  assert(size(37) == 'S')
  assert(size(38) == 'L')
  assert(size(40) == 'M')
  assert(size(42) == 'L')
  assert(size(43) == 'L')
  assert(size(37.9) == 'S')
  assert(size(38.1) == 'M')
  assert(size(41.9) == 'M')
  assert(size(42.1) == 'L')
