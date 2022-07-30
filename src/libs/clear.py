import sys
import os


def repeat(val, times):
  res = ''

  for x in range(times):
    ret += val

  return res


def clear(start, end):
  columns, lines = os.get_terminal_size(0)
  fill = repeat(' ', columns)

  for x in range(start, end):
    print(fill)


sys.modules[__name__] = clear