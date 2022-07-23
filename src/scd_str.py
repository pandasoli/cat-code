import sys
import re
import os


class main:
  str = ''
  scdline = ''
  scdline_colors = []
  program_dir = os.path.dirname(os.path.realpath(__file__))

  def whereis(self, text, value) -> list:
    res = []

    for x in range(0, len(text)):
      if text[x:x + len(value)] == value:
        res.append(x)

    return res

  def rmdup(self, arr) -> list:
    res = []

    for item in arr:
      if item not in res:
        res.append(item)

    return res

  def insertat(self, arr, item, at) -> list:
    res = []

    for x in range(0, len(arr)):
      if x == at:
        res.append(item)
      res.append(arr[x])

    return res


  def __init__(self, str = '') -> None:
    self.setStr(str)


  def show(self) -> None:
    print(f'first line   : "{self.str}"')
    print(f'second line  : "{self.scdline}"')
    print(f'joined lines : "{self.join()}"')

  def add(self, text, pos) -> None:
    color_regex = r'\033\[[0-9;]+m'

    colors = re.findall(color_regex, text)
    formatedText = re.sub(color_regex, '', text)

    self.scdline = self.scdline[:pos] + formatedText + self.scdline[pos + len(formatedText):]

    for color in self.rmdup(colors):
      for po in self.whereis(text, color):
        if len(self.scdline_colors) == 0:
          self.scdline_colors.append({
            'value': color,
            'pos': pos
          })
        else:
          for x in range(0, len(self.scdline_colors)):
            if self.scdline_colors[x]['pos'] > po + len(self.scdline[:pos]):
              self.scdline_colors = self.insertat(
                self.scdline_colors,
                { 'value': color, 'pos': po + len(self.scdline[:pos]) },
                x
              )
              break

            if x == len(self.scdline_colors) - 1:
              self.scdline_colors.append({
                'value': color,
                'pos': po + len(self.scdline[:pos])
              })

  def remove(self, start, end) -> None:
    cleanVal = ''

    for x in range(0, len(self.scdline_colors)):
      if self.scdline_colors[x]['pos'] > start and self.scdline_colors[x]['pos'] < end:
        self.scdline_colors.pop(x)

    for x in range(start, end):
      cleanVal += ' '

    self.scdline = self.scdline[:start] + cleanVal + self.scdline[end:]

  def removeColors(self, start, end) -> None:
    n = []

    for color in self.scdline_colors:
      if color['pos'] <= start or color['pos'] > end:
        n.append(color)

    self.scdline_colors = n

  def join(self) -> str:
    res = ''

    for x in range(0, len(self.scdline)):
      ch = self.scdline[x]

      if ch == ' ':
        res += self.str[x]
      else:
        res += self.scdline[x]

    sumOfColors = 0
    for color in self.scdline_colors:
      res = res[:color['pos'] + sumOfColors] + color['value'] + res[color['pos'] + sumOfColors:]
      sumOfColors += len(color['value'])

    return res


  def setStr(self, str) -> None:
    self.str = str
    self.scdline = ''

    for x in range(0, len(str)):
      self.scdline += ' '


sys.modules[__name__] = main