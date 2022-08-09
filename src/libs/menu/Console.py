import sys
import os
from os import system
from os import path


class Cursor:
  program_dir = path.dirname(path.realpath(__file__))
  pos = { 'x': 0, 'y': 0 }

  def __init__(self):
    self.get()

  def visible(self, value):
    if value: system('tput cnorm')
    else: system('tput civis')

  def set(self, x, y):
    system(f'tput cup {y} {x}')

    self.pos['x'] = x
    self.pos['y'] = y

  def get(self):
    file = open(f'{self.program_dir}/get-cur-pos.sh', 'w')
    file.write('#!/bin/bash\nexec < /dev/tty\noldstty=$(stty -g)\nstty raw -echo min 0\necho -en "\033[6n" > /dev/tty\nIFS=\';\' read -r -d R -a pos\nstty $oldstty\nrow=$((${pos[0]:2} - 1))\ncol=$((${pos[1]} - 1))\necho $col:$row')
    file.close()

    res = os.popen(f'/bin/bash {self.program_dir}/get-cur-pos.sh').read()

    self.pos['x'] = int( res.split(':')[0] )
    self.pos['y'] = int( res.split(':')[1] )

    return self.pos


class Console:
  program_dir = path.dirname(path.realpath(__file__))
  cursor = Cursor()
  columns = 0
  rows = 0

  def __init__(self):
    file = open(f'{self.program_dir}/get-con-size.sh', 'w')
    file.write('echo "$(tput cols):$(tput lines)"')
    file.close()

    res = os.popen(f'/bin/bash {self.program_dir}/get-con-size.sh').read()

    self.columns = int( res.split(':')[0] )
    self.rows = int( res.split(':')[1] )


sys.modules[__name__] = Console