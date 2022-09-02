import sys
import re
import yaml
from os import path
from types import NoneType

import openf
from lexer import Lexer, TokenKind


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

  config = {}

  def __init__(self) -> None:
    config_file = openf(f'{self.program_dir}/config.yml')

    if config_file.status == False:
      print('')
      print('\033[1;31m◈ Dependency not found')
      print(f'  \033[0;31mNot found: \033[0m{self.program_relative_dir}/config.yml')
      print('')

      exit()

    self.config = yaml.safe_load(config_file.content)
    theme = self.config['theme']
    theme_file = openf(f'{self.program_dir}/themes/{theme}.yml')

    if theme_file.status == False:
      print('')
      print('\033[1;31m◈ Dependency not found')
      print(f'  \033[0;31mNot found: \033[0m{self.program_relative_dir}/themes/{theme}.yml')
      print('')

      exit()

    self.config['theme'] = yaml.safe_load(theme_file.content)


  # { status: int, warnings: list<str>, res: str }
  def text(self, text, ext = 'txt') -> dict:
    res = { 'status': 0, 'warnings': [], 'res': '' }

    if ext == 'txt':
      res['res'] = text
      return res

    config = self.loadConfig(
      self.config['extensions'][ext] if ext in self.config['extensions'] else ext
    )
    tokens = Lexer(text, config['config']).lex()
    code = ''

    string_cl     = self.config['theme']['string']
    bracket_cl    = self.config['theme']['bracket']
    number_cl     = self.config['theme']['number']
    mathchar_cl   = self.config['theme']['mathchar']
    important_cl  = self.config['theme']['important']
    keyword_cl    = self.config['theme']['keyword']
    comment_cl    = self.config['theme']['comment']
    warning_cl    = self.config['theme']['warning']
    error_cl      = self.config['theme']['error']
    identifier_cl = self.config['theme']['identifier']
    unknown_cl    = self.config['theme']['unknown']
    space_cl      = self.config['theme']['space']

    for tk in tokens:
      print('"' + tk.literal + '"', tk.kind)
      if   tk.kind == TokenKind.String:     code += f'\033[{string_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Bracket:    code += f'\033[{bracket_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Number:     code += f'\033[{number_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.MathChar:   code += f'\033[{mathchar_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Important:  code += f'\033[{important_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.KeyWord:    code += f'\033[{keyword_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Comment:    code += f'\033[{comment_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Warning:    code += f'\033[{warning_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Error:      code += f'\033[{error_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Identifier: code += f'\033[{identifier_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Space:      code += f'\033[{space_cl}m{tk.literal}\033[0m'
      elif tk.kind == TokenKind.Unknown:    code += f'\033[{unknown_cl}m{tk.literal}\033[0m'

    if len(config['warnings']) > 0: res['status'] = 2
    res['res'] = code
    res['warnings'] = config['warnings']
    return res

  # { status: int, warnings: list<str>, res: str }
  def file(self, file, lang = '') -> dict:
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


  def show(self, file, content) -> str:
    lines = [
      '',
      f'\033[1;32m✔ {file}:',
      '\033[32m➤\033[0m ' + '\n  '.join(content.split('\n')),
      ''
    ]

    return '\033[0m\n'.join(lines)

  def warn(self, file, content, msgs) -> str:
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

  def error(self, file, msg) -> str:
    lines = [
      '',
      f"\033[1;31m✗ {file}: \033[0;31m{msg}",
      ''
    ]

    return '\033[0m\n'.join(lines)


  # { warnings: list<str>, config: ... } }
  def loadConfig(self, ext) -> dict:
    warnings = []
    config = {}

    # ◈ Openning
    config = openf(f'{self.program_dir}/langs/{ext}.yml')
    if config.status == False:
      config = { 'colors': [], 'groups': [] }

      warnings.append('Not found syntax file')
      return {
        'warnings': warnings,
        'config': config
      }

    config = yaml.safe_load(config.content)

    if type(config) is NoneType:
      config = {}

    return {
      'warnings': warnings,
      'config': config
    }


sys.modules[__name__] = highlight