import sys
import re

from libs.menu import Getch
from libs.menu import Cursor


def loopItem(arr):
  return zip(range(len(arr)), arr)

def repeat(str, times):
  res = ''

  for x in range(0, times + 1):
    res += str

  return res


class menu:
  items = []
  top = 0
  cursor = None
  status = False
  title = ''
  selected = {
    'last': 0,
    'current': 0
  }

  def __init__(self, title, items, showTitle = True):
    if showTitle:
      print(f'\033[1;34m◈ {title}:\033[0m')

    self.title = f'◈ {title}:'
    self.items = []
    self.status = False
    self.cursor = Cursor()
    self.top = self.cursor.get()['y']

    self.cursor.visible(False)

    for x, item in loopItem(items):
      self.items.append({ 'value': item, 'pos': self.top + x })

    self.load()
    self.loop()
    self.end(showTitle)

    self.cursor.set(0, self.top)
    self.cursor.visible(True)


  def end(self, showTitle = True):
    for x, item in loopItem(self.items):
      value = item['value']
      pos = item['pos']

      self.cursor.set(0, pos)
      print(repeat(' ', len(value)))

    if showTitle:
      self.cursor.set(0, self.top - 1)

      if self.status:
        print('\033[1;34m✔\033[0m')

        self.cursor.set(len(self.title) + 1, self.top - 1)
        print( self.items[self.selected['current']]['value'] )
      else:
        print('\033[1;34m✗\033[0m')


  def loop(self):
    key = ''
    stopKeys = [ 13, 32, 113 ]
    getch = Getch()

    while key not in stopKeys:
      key = getch()

      self.selected['last'] = self.selected['current']

      if key == 24 and self.selected['current'] > 0:
        self.selected['current'] -= 1
      elif key == 25 and self.selected['current'] < len(self.items) - 1:
        self.selected['current'] += 1

      self.reload()

    if key != 113:
      self.status = True


  def reload(self):
    last = self.items[self.selected['last']]
    current = self.items[self.selected['current']]

    self.cursor.set(0, last['pos'])
    print('\033[37m', last['value'], '\033[0m', sep = '')

    self.cursor.set(0, current['pos'])
    print('\033[4;37m', current['value'], '\033[0m', sep = '')

  def load(self):
    for key, item in loopItem(self.items):
      value = item['value']
      pos = item['pos']

      self.cursor.set(0, pos)

      if key == self.selected['current']:
        print(f'\033[4;37m{value}\033[0m')
      else:
        print(f'\033[37m{value}\033[0m')



sys.modules[__name__] = menu