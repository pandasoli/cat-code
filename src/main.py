#!/usr/bin/python3

import re
import os
import sys
import yaml
from types import NoneType
from os import path

import help
import scd_str

'''
  Created by Panda Soli

  Repo: https://github.com/pandasoli/cat-code
  Contacts:
    Whatsapp: +55 51 9380 3517
    Instagram: @pandasoli.ofc
    Facebook: pandasoli.ofc
    Github: pandasoli
'''

def openf(local, do = lambda content: print(content)):
  if not path.exists(local):
    print(f"\033[1;31m{local}\033[0m: Doesn't exist")
    exit()
  else:
    with open(local, 'r') as content:
      return do(content)

def main():
  program_dir = os.path.dirname(os.path.realpath(__file__))

  for file in sys.argv[1:]:
    splited = file.split('.')
    extension = splited[len(splited) - 1]
    config = {}

    print('')

    if file == '--help' or file == '-h':
      help()
      continue

    def loadConfig(content):
      list = yaml.safe_load(content)
      config = {}
      at = extension

      def setConfig(content):
        config = yaml.safe_load(content)

        if type(config) is NoneType:
          config = {}

        def error(message):
          print(f'\033[1;31m◈ {file}')
          print(f'  \033[0;31m{at}.yml\033[37m: Got an unexpected architecture')
          print(f'  {message}')
          print('')
          print('  \033[1;37m◈ To more help')
          print('    \033[0;31mcatc \033[33m--help\033[0m')
          print('')
          return False

        if not 'colors' in config.keys():
          config['colors'] = {}
        elif type(config['colors']) is not dict:
          return error("Colors isn't an object")

        if not 'groups' in config.keys():
          return error("There's no groups object")
        # elif type(config['groups']) is not list:
          # return error("Groups isn't a list")

        for group in config['groups']:
          if not 'color' in group.keys():
            return error("There's a group with no color")
          if not 'regex' in group.keys() and not 'regexes' in group.keys():
            return error("There's a group without regex and regexes")

        for x in range(0, len(config['groups'])):
          group = config['groups'][x]

          if len( re.findall(r'^[0-9;]+$', str(group['color'])) ) == 0:
            if group['color'] in config['colors'].keys():
              config['groups'][x]['color'] = config['colors'][group['color']]
            else:
              config['groups'][x]['color'] = 37

        return config

      if extension in list:
        at = list[extension]

      config = openf(f'{program_dir}/langs/{at}.yml', setConfig)
      return config

    config = openf(f'{program_dir}/extensions.yml', loadConfig)

    if config == False:
      continue

    with open(file, 'r') as content:
      code = scd_str(''.join(content.readlines()) + '\n')

      for group in config['groups']:
        color = group['color']
        regexes = []

        if 'regex' in group.keys():
          regexes.append(group['regex'])

        if 'regexes' in group.keys():
          regexes += group['regexes']

        for regex in regexes:
          matches = code.rmdup(re.findall(regex, code.str))

          for match in matches:
            poses = code.whereis(code.str, match)

            for pos in poses:
              code.removeColors(pos, pos + len(match))

              code.add(f'\033[{color}m', pos)
              code.add(f'\033[0m', pos + len(match))

      print(f'\033[1;32m◈ {file}\033[0m:')
      print('  ' + '\n  '.join(code.join().split('\n')))

if __name__ == '__main__':
  main()
