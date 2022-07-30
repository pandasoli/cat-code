import sys
import re
import yaml
from os import path
from types import NoneType

import openf
import sstr


def whereis(text, value) -> list:
  res = []

  for x in range(0, len(text)):
    if text[x:x + len(value)] == value:
      res.append(x)

  return res

def rmdup(arr) -> list:
  res = []

  for item in arr:
    if item not in res:
      res.append(item)

  return res


class highlight:
  user_path = path.expanduser('~')
  program_dir = path.dirname(path.realpath(__file__))
  program_relative_dir = re.sub(fr'^{user_path}', '~', program_dir)

  extensions = {}

  current = {
    'file': '',
    'config-file': '',
    'config': {}
  }

  def __init__(self) -> None:
    ofile = openf(f'{self.program_dir}/extensions.yml')

    if ofile.status == False:
      print('')
      print('\033[1;31m◈ Dependency not found')
      print(f'  \033[0;31mNot found: \033[0m{self.program_relative_dir}/extensions.yml')
      print('')

      exit()

    self.extensions = yaml.safe_load(ofile.content)


  # { status: int, warnings: list<str>, res: str }
  def text(self, text, lang = 'txt'):
    res = { 'status': 0, 'warnings': [], 'res': '' }

    if lang == 'txt':
      res['res'] = text
      return res

    extensions = yaml.safe_load( openf(f'{self.program_dir}/extensions.yml').content )
    self.current['config-file'] = extensions[lang] if lang in extensions else lang

    warnings = self.loadConfig()
    code = sstr(text)
    config = self.current['config']

    for group in config['groups']:
      color = group['color']
      rewrite = group['rewrite']
      regexes = []

      if 'regex' in group.keys():
        regexes.append(group['regex'])

      if 'regexes' in group.keys():
        regexes += group['regexes']

      for regex in regexes:
        matches = rmdup(re.findall(regex, code.str))

        for match in matches:
          poses = whereis(code.str, match)

          for pos in poses:
            if rewrite:
              code.remove(pos, pos + len(match))
            else:
              code.replace(f'\033[{color}m', pos, pos + len(match))

            code.add(f'\033[{color}m', pos)
            code.add(f'\033[0m', pos + len(match))

    if len(warnings) > 0: res['status'] = 2
    res['res'] = code.join()
    res['warnings'] = warnings
    return res

  # { status: int, warnings: list<str>, res: str }
  def file(self, file, lang = ''):
    self.current['file'] = file
    res = { 'status': True, 'warnings': [], 'res': '' }

    fopen = openf(file)

    if fopen.status == False:
      res['status'] = 1
      return res

    res = self.text(
      fopen.content,
      file.split('.')[-1] if lang == '' else lang
    )

    return res


  # str
  def show(self, content):
    file = self.current['file']

    lines = [
      '',
      f'\033[1;32m✔ {file}:',
      '\033[32m➤\033[0m ' + '\n  '.join(content.split('\n')),
      ''
    ]

    return '\033[0m\n'.join(lines)

  # str
  def warn(self, content, msgs):
    file = self.current['file']
    msgs_begin = 0

    lines = [
      '',
      f'\033[1;33m⚠ {file}:',
    ]

    if msgs[0] == 'Not found syntax file':
      lines[-1] += ' \033[0;33mNot found syntax file'
      msgs_begin = 1

    for x in range(msgs_begin, len(msgs)):
      msg = msgs[x]
      lines.append(f'\033[33m╰─➤ {msg}')

    if len(msgs) > 0 and msgs_begin == 0:
      lines.append('')

    lines.append('\033[33m➤\033[0m ' + '\n  '.join(content.split('\n')))
    lines.append('')
    return '\033[0m\n'.join(lines)

  # str
  def error(self, msg):
    file = self.current['file']

    lines = [
      '',
      f"\033[1;31m✗ {file}: \033[0;31m{msg}",
      ''
    ]

    return '\033[0m\n'.join(lines)


  # list<str>
  def loadConfig(self):
    configfile = self.current['config-file']
    warnings = []
    config = {}

    config = openf(f'{self.program_dir}/langs/{configfile}.yml')
    if config.status == False:
      config = { 'colors': [], 'groups': [] }
      self.current['config'] = config

      warnings.append('Not found syntax file')
      return warnings

    config = yaml.safe_load(config.content)

    if type(config) is NoneType:
      config = {}

    # ◈ Validatting
    if not 'colors' in config.keys():
      config['colors'] = {}
    elif type(config['colors']) is not dict:
      config['colors'] = {}
      warnings.append("Colors isn't an object")

    if not 'groups' in config.keys():
      config['groups'] = {}
      warnings.append("There's no groups list")
    elif type(config['groups']) is not list:
      config['groups'] = []
      warnings.append("Groups isn't a list")

    for x in range(0, len(config['groups'])):
      group = config['groups'][x]

      if not 'color' in group.keys():
        config['groups'][x]['color'] = 37
        warnings.append("There's a group with no color")
      if not 'rewrite' in group.keys():
        config['groups'][x]['rewrite'] = True
      if not 'regex' in group.keys() and not 'regexes' in group.keys():
        config['groups'][x]['regex'] = ''
        warnings.append("There's a group without regex and regexes")

    # ◈ Calling color variables
    for x in range(0, len(config['groups'])):
      group = config['groups'][x]

      if len( re.findall(r'^[0-9;]+$', str(group['color'])) ) == 0:
        if group['color'] in config['colors'].keys():
          config['groups'][x]['color'] = config['colors'][group['color']]
        else:
          config['groups'][x]['color'] = 37

    self.current['config'] = config
    return warnings


sys.modules[__name__] = highlight