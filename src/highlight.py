import sys
import re
import yaml
from os import path
from types import NoneType

import openf
from lexer import Lexer, TokenKind
# import sstr


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

def loop(arr):
  return zip(range(len(arr)), arr)


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
  def text(self, text, ext = 'txt') -> dict:
    res = { 'status': 0, 'warnings': [], 'res': '' }

    if ext == 'txt':
      res['res'] = text
      return res

    extensions = yaml.safe_load( openf(f'{self.program_dir}/extensions.yml').content )
    self.current['config-file'] = extensions[ext] if ext in extensions else ext

    config = self.loadConfig()
    tokens = Lexer(text, config['config']).lex()
    code = ''

    for tk in tokens:
      if   tk.kind == TokenKind.String:      code += f'\033[32m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Bracket:     code += f'\033[2;36m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Number:      code += f'\033[33m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.MathChar:    code += f'\033[36m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Important:   code += f'\033[31m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.KeyWord:     code += f'\033[2;35m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Comment:     code += f'\033[1;30m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Warning:     code += f'\033[4;33m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Error:       code += f'\033[4;31m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Identifier:  code += f'\033[35m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Unknown:     code += f'\033[0m{tk.literal}\033[0m'

    if len(config['warnings']) > 0: res['status'] = 2
    res['res'] = code
    res['warnings'] = config['warnings']
    return res

  # { status: int, warnings: list<str>, res: str }
  def file(self, file, lang = '') -> dict:
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


  def show(self, content) -> str:
    file = self.current['file']

    lines = [
      '',
      f'\033[1;32m✔ {file}:',
      '\033[32m➤\033[0m ' + '\n  '.join(content.split('\n')),
      ''
    ]

    return '\033[0m\n'.join(lines)

  def warn(self, content, msgs) -> str:
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

  def error(self, msg) -> str:
    file = self.current['file']

    lines = [
      '',
      f"\033[1;31m✗ {file}: \033[0;31m{msg}",
      ''
    ]

    return '\033[0m\n'.join(lines)


  # { warnings: list<str>, config: ... } }
  def loadConfig(self) -> dict:
    configfile = self.current['config-file']
    warnings = []
    config = {}

    # ◈ Openning
    config = openf(f'{self.program_dir}/langs/{configfile}.yml')
    if config.status == False:
      config = { 'colors': [], 'groups': [] }
      self.current['config'] = config

      warnings.append('Not found syntax file')
      return warnings

    config = yaml.safe_load(config.content)

    if type(config) is NoneType:
      config = {}

    return {
      'warnings': warnings,
      'config': config
    }


sys.modules[__name__] = highlight