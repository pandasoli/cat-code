import sys
import os
from os import system
from os import path

# get-cur-pos.sh
'''
#!/bin/bash

exec < /dev/tty
oldstty=$(stty -g)
stty raw -echo min 0

echo -en "\033[6n" > /dev/tty

IFS=';' read -r -d R -a pos
stty $oldstty

row=$((${pos[0]:2} - 1))
col=$((${pos[1]} - 1))
echo $col:$row
'''


class Cursor:
  program_dir = path.dirname(path.realpath(__file__))
  pos = {
    'x': 0,
    'y': 0
  }

  def __init__(self):
    self.get()

  def visible(self, value):
    if value:
      system('tput cnorm')
    else:
      system('tput civis')

  def set(self, x, y):
    system(f'tput cup {y} {x}')

    self.pos['x'] = x
    self.pos['y'] = y

  def get(self):
    res = os.popen(f'/bin/bash {self.program_dir}/get-cur-pos.sh').read()

    self.pos['x'] = int( res.split(':')[0] )
    self.pos['y'] = int( res.split(':')[1] )

    return self.pos


sys.modules[__name__] = Cursor