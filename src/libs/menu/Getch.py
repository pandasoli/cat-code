import sys


class Getch:
  def __init__(self):
    try:
        self.impl = _GetchWindows()
    except ImportError:
        self.impl = _GetchUnix()

  def __call__(self):
    key = self.impl()

    if key == '\x1b':
      keys = {
        '[A': 24,
        '[B': 25,
        '[C': 26,
        '[D': 27
      }

      key = keys[self.impl() + self.impl()]
    else:
      key = ord(key)

    return key


class _GetchUnix:
  def __init__(self):
    import tty
    import sys

  def __call__(self):
    import tty
    import sys
    import termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


class _GetchWindows:
  def __init__(self):
    import msvcrt

  def __call__(self):
    import msvcrt

    return msvcrt.getch().decode('utf-8')


sys.modules[__name__] = Getch