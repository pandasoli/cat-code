#!/usr/bin/python3

import sys

import help
import sstr
import openf
import highlight


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
  if len(sys.argv) == 1:
    lines = [
      '',
      f'\033[1;31m✗ No params found:',
      '  Type \033[31mcatc \033[33m--help\033[0m for help',
      ''
    ]

    for line in lines:
      print(f'{line}\033[0m')
    exit()

  code = highlight()

  for file in sys.argv[1:]:
    if file == '--help' or file == '-h':
      help()
    else:
      splited = file.split(':')
      file = splited[0]
      syntax = ''

      if len(splited) > 1:
        syntax = splited[1]

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
