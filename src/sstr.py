import sys
import re


def insertat(arr, item, at) -> list:
  res = []

  for x in range(0, len(arr)):
    if x == at:
      res.append(item)
    res.append(arr[x])

  return res


class main:
  str = ''
  colors = []

  def __init__(self, str) -> None:
    self.str = str

  def add(self, cl, pos) -> None:
    color_regex = r'\033\[[0-9;]+m'
    content = {
      'value': cl,
      'pos': pos
    }

    if len(self.colors) == 0 or self.colors[-1]['pos'] < pos:
      self.colors.append(content)
      return

    for x in range(0, len(self.colors)):
      color = self.colors[x]

      if color['pos'] > pos:
        self.colors = insertat(self.colors, content, x)
        break

  def remove(self, start, end) -> None:
    res = []

    for color in self.colors:
      if color['pos'] < start or color['pos'] > end:
        res.append(color)

    self.colors = res

  def join(self) -> str:
    res = self.str

    sumOfColors = 0
    for color in self.colors:
      res = res[:color['pos'] + sumOfColors] + color['value'] + res[color['pos'] + sumOfColors:]
      sumOfColors += len(color['value'])

    return res


sys.modules[__name__] = main