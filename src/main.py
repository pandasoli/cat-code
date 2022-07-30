#!/usr/bin/python3

import sys

import help
import sstr
import openf
import highlight
from os.path import isfile


'''
  Created by Panda Soli

  Repo: https://github.com/pandasoli/cat-code
  Contacts:
    Whatsapp: +55 51 9380 3517
    Instagram: @pandasoli.ofc
    Facebook: pandasoli.ofc
    Github: pandasoli
'''

def main():
  code = highlight()

  if len(sys.argv) == 1:
    lines = [
      '',
      f'\033[1;31m✗ No params found:',
      '  Type ' + code.text('catc --help', 'bash')['res'] + ' for help',
      ''
    ]

    for line in lines:
      print(f'{line}\033[0m')
    exit()

  for file in sys.argv[1:]:
    splited = file.split(':')
    file = splited[0]
    syntax = ''

    if len(splited) > 1:
      syntax = splited[1]

    if file == '--help' or file == '-h':
      help(syntax)
    elif isfile(file) == False:
      code.current['file'] = file

      print(
        code.error('Is not a file')
      )
    else:
      res = code.file(file, syntax)

      if res['status'] == 0:
        print(
          code.show(res['res'])
        )
      elif res['status'] == 1:
        print(
          code.error("Doesn't found")
        )
      elif res['status'] == 2:
        print(
          code.warn(res['res'], res['warnings'])
        )


if __name__ == '__main__':
  main()
