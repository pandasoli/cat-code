#!/usr/bin/python3

import sys
import re
import yaml
from types import NoneType
from os import path

import help
import scd_str
import openf


'''
  Created by Panda Soli

  Repo: https://github.com/pandasoli/cat-code
  Contacts:
    Whatsapp: +55 51 9380 3517
    Instagram: @pandasoli.ofc
    Facebook: pandasoli.ofc
    Github: pandasoli
'''


class main:
  user_path = path.expanduser('~')
  program_dir = path.dirname(path.realpath(__file__))
  program_relative_dir = re.sub(fr'^{user_path}', '~', program_dir)

  current = {
    'file': '',
    'extension': '',
    'config-file': '',
    'config': {}
  }

  def __call__(self, file) -> None:
    if file == '--help' or file == '-h':
      help()
      return

    self.current['file'] = file
    self.current['extension'] = file.split('.')[-1]

    extension = self.current['extension']
    extensions = yaml.safe_load( openf(f'{self.program_dir}/extensions.yml').content )

    self.current['config-file'] = extensions[extension] if extension in extensions else extension
    configStatus = self.loadConfig() 


    content = openf(file).content
    code = scd_str(content)
    config = self.current['config']

    if configStatus != 0:
      if configStatus == 2:
        self.show(content, False)
      return

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

    self.show(code.join())

  def show(self, content, foundHL = True) -> None:
    file = self.current['file']

    print('')
    print(f'\033[1;32m◈ {file}\033[0m:', end = '')

    if foundHL == False:
      print(f" \033[33mNo highlight found\033[0m")
    else:
      print('')

    print('  ' + '\n  '.join(content.split('\n')))
    print('')

  def error(self, message) -> 1:
    file = self.current['file']
    configfile = self.current['config-file']

    lines = [
      '',
      f'\033[1;31m◈ {file}',
      f'  \033[0;31m{self.program_relative_dir}/langs/{configfile}.yml\033[37m: Got an unexpected architecture',
      f'  {message}',
      '',
      '  \033[1;37m◈ To more help',
      '    \033[0;31mcatc \033[33m--help\033[0m',
      ''
    ]

    for line in lines:
      print(line)

    return 1

  def loadConfig(self) -> int:
    configfile = self.current['config-file']
    config = {}

    config = openf(f'{self.program_dir}/langs/{configfile}.yml')
    if config.status == False: return 2

    config = yaml.safe_load( config.content )

    # ◈ Validatting
    if not 'colors' in config.keys():
      config['colors'] = {}
    elif type(config['colors']) is not dict:
      return self.error("Colors isn't an object")

    if not 'groups' in config.keys():
      return self.error("There's no groups object")
    # elif type(config['groups']) is not list:
      # return error("Groups isn't a list")

    for group in config['groups']:
      if not 'color' in group.keys():
        return self.error("There's a group with no color")
      if not 'regex' in group.keys() and not 'regexes' in group.keys():
        return self.error("There's a group without regex and regexes")

    # ◈ Calling color variables
    for x in range(0, len(config['groups'])):
      group = config['groups'][x]

      if len( re.findall(r'^[0-9;]+$', str(group['color'])) ) == 0:
        if group['color'] in config['colors'].keys():
          config['groups'][x]['color'] = config['colors'][group['color']]
        else:
          config['groups'][x]['color'] = 37

    self.current['config'] = config
    return 0


if __name__ == '__main__':
  fun = main()

  for file in sys.argv[1:]:
    fun(file)
