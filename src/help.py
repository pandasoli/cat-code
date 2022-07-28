import sys


def main():
  lines = [
    '',
    '🐈 \033[1;32mCat Code\033[0m 🖤',
    'Repo: \033[36mhttps://github.com/pandasoli/cat-code',
    '',
    '◈ \033[1;37mWho made: \033[33mPanda Soli',
    '  Whatsapp: \033[36m+55 51 9380 3517',
    '  Instagram: \033[36m@pandasoli.ofc',
    '  Facebook: \033[36mpandasoli.ofc',
    '  Github: \033[36mpandasoli',
    '',
    '◈ \033[1;37mHow to use',
    '  \033[31mcatc \033[33m<...files>',
    '',
    '◈ \033[1;37mHow to create your own highlight',
    "Create a file called like 'lang.yml' in /langs",
    'Its template must be:',
    '  \033[31mcolors\033[37m: \033[30m# optional',
    '    \033[30m# your color variables',
    '    \033[31mred\033[37m: \033[33m31',
    '    \033[31mblue\033[37m: \033[33m34',
    '',
    '  \033[31mregexes\033[37m:',
    "    - \033[31mcolor\033[37m: \033[32m'red'      \033[30m# calling a color variable",
    '      \033[31mregexes\033[37m:          \033[30m# this can be a list or not',
    "        - \033[32m'\\bfalse'",
    "        - \033[32m'\\btrue'",
    '',
    "    - \033[31mcolor\033[37m: \033[33m34         \033[30m# blue color (doesn't call a variable)",
    "      \033[31mregex\033[37m: \033[32m'[a-zA-Z]'",
    '',
    'If your language has more than one extenssion,',
    'in the file extensions.yml put this:',
    '  \033[30m# "<extenssion>": "name of the yaml created at /langs"',
    "  \033[30m# OBS: it's not necessary the file name.",
    '  \033[31mc\033[37m: \033[32mcpp',
    '  \033[31mh\033[37m: \033[32mcpp',
    ''
  ]

  for line in lines:
    print(f'{line}\033[0m')


sys.modules[__name__] = main