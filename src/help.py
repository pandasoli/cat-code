import sys

import highlight
from libs.menu import menu


ccode = highlight().text

def main(page = ''):
  def showPage(page):
    lines = []

    if page == 0: lines = credits()
    elif page == 1: lines = howuse()
    elif page == 2: lines = createhighlight()

    for line in lines:
      print(f'{line}\033[0m')

    print('')

  print(
    '',
    '🐈‍⬛️ \033[1;32mCat Code\033[0m 🖤',
    'Repo: \033[36mhttps://github.com/pandasoli/cat-code',
    '',
    sep = '\033[0m\n'
  )

  if page != '':
    id = -1

    if page == 'who': id = 0
    if page == 'how': id = 1
    if page == 'light': id = 2

    if id > -1:
      showPage(id)
      return

  item = menu(
    '',
    [
      '◈ \033[1;37mWho made: \033[33mPanda Soli',
      '◈ \033[1;37mHow to use',
      '◈ \033[1;37mHow to create your own highlight'
    ],
    False
  )

  if item.status:
    showPage(item.selected['current'])
  else:
    print(
      "◈ \033[1;37mIf menu didn't work use:",
      '  ' + ccode('catc -h:who', 'bash')['res'],
      '  ' + ccode('catc -h:how', 'bash')['res'],
      '  ' + ccode('catc -h:light', 'bash')['res'],
      '',
      sep = '\033[0m\n'
    )

def credits():
  return [
    '◈ \033[1;37mWho made: \033[33mPanda Soli',
    '  Whatsapp: \033[36m+55 51 9380 3517',
    '  Instagram: \033[36m@pandasoli.ofc',
    '  Facebook: \033[36mpandasoli.ofc',
    '  Github: \033[36mpandasoli'
  ]

def howuse():
  return [
    '◈ \033[1;37mHow to use',
    '  \033[31mcatc \033[33m...<file>:<?syntax>'
  ]

def createhighlight():
  codes = {
    'langs': [
      '  colors: # optional',
      '    # your color variables',
      '    red: 31',
      '    blue: 34',
      '',
      '  regexes:',
      "    - color: 'red'      # calling a color variable",
      '      regexes:          # this can be a list or not',
      "        - '\\bfalse'",
      "        - '\\btrue'",
      '',
      "    - color: 34         # blue color (doesn't call a variable)",
      "      regex: '[a-zA-Z]'"
    ],
    'extensions': [
      '  # "<extenssion>": "name of the yaml created at /langs"',
      "  # OBS: it's not necessary the file name.",
      '  c: cpp',
      '  h: cpp'
    ]
  }

  for code in codes.keys():
    codes[code] = '\n'.join(codes[code])

  return [
    '◈ \033[1;37mHow to create your own highlight',
    "Create a file called like 'lang.yml' in /langs",
    'Its template must be:',
    ccode(codes['langs'], 'yaml')['res'],
    '',
    'If your language has more than one extenssion,',
    'in the file extensions.yml put this:',
    ccode(codes['extensions'], 'yaml')['res'],
  ]


sys.modules[__name__] = main