import sys
import re
import yaml
import os

import scd_str


def main():
  program_dir = os.path.dirname(os.path.realpath(__file__))

  for file in sys.argv[1:]:
    splited = file.split('.')
    extension = splited[len(splited) - 1]
    config = {}

    with open(f'{program_dir}/extensions.yml', 'r') as content:
      list = yaml.safe_load(content)

      if extension in list:
        at = list[extension]

        with open(f'{program_dir}/langs/{at}.yml', 'r') as content:
          config = yaml.safe_load(content)
      else:
        with open(f'{program_dir}/langs/{extension}.yml', 'r') as content:
          config = yaml.safe_load(content)

    with open(file, 'r') as content:
      code = scd_str(''.join(content.readlines()) + '\n')

      for group in config['groups']:
        color = group['color']

        matches = code.rmdup(re.findall(group['regex'], code.str))

        for match in matches:
          for pos in code.whereis(code.str, match):
            code.removeColors(pos, pos + len(match))

            code.add(f'\033[{color}m', pos)
            code.add(f'\033[0m', pos + len(match))

      print(code.join())

if __name__ == '__main__':
  main()
