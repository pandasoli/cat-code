import sys

class main:
  str = ''
  res = ''
  _addeds = []
  # {
  #   value: string
  #   start: number
  # }

  def __init__(self, str):
    self.setStr(str)

  def add(self, value, start):
    nStart = start

    for x in self._addeds:
      if x['start'] <= start:
        nStart += len(x['value'])

    self._addeds.append({ 'value': value, 'start': start })
    self.res = self.res[:nStart] + value + self.res[nStart:]

  def remove(self, start, end):
    for x in range(0, self._addeds):
      
    # new = []

    # for x in self._addeds:
    #   if x['start'] < start or x['start'] > end:
    #     new.append(x)

    # self._addeds = new

  def setStr(self, str):
    self.str = str
    self.res = str
    self._addeds = []

sys.modules[__name__] = main