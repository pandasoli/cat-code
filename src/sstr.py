import sys
import re


class sstr:
  str = ''
  colors = {}

  def __init__(self, str):
    self.str = str
    self.colors = {}

  def add(self, cl, pos):
    self.colors[pos] = cl

  def remove(self, start, end):
    for x in range(start, end):
      if x in self.colors:
        del self.colors[x]

  def join(self) -> str:
    res = self.str
    colors = dict( self.colors )
    csum = 0

    def getmin(arr):
      res = arr[0]

      for item in arr:
        if item < res:
          res = item

      return res

    for _ in self.colors.items():
      ps = getmin(list(colors.keys()))
      cl = colors[ps]

      res = res[:ps + csum] + cl + res[ps + csum:]
      csum += len(cl)

      del colors[ps]

    # f = open('[scd_str] join res.cache.txt', 'w')
    # f.write(res)
    # f.close()

    return res


sys.modules[__name__] = sstr