import sys
from os import path


class openf:
  content = ''
  status = False

  def __init__(self, filePath) -> bool:
    self.content = ''

    if path.exists(filePath):
      f = open(filePath, 'r')

      self.content = ''.join( f.readlines() )
      self.status = True

      f.close()
    else:
      self.status = False

  def print(self) -> None:
    print(self.content)


sys.modules[__name__] = openf