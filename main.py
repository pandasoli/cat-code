#!/usr/bin/env python3

from pickle import FALSE
import sys
import yaml
import re
import opacity_str

def arrRemDup(arr):
  res = []

  for item in arr:
    if item not in res:
      res.append(item)

  return res

def whereare(str, text):
  res = []

  for x in range(0, len(str)):
    if str[x:x + len(text)] == text:
      res.append(x)

  return res

def main():
  files = {}

  for file in sys.argv[1:]:
    splited = file.split('.')
    extension = splited[len(splited) - 1]
    files[file] = { 'code': '', 'lookat': '' }

    with open('extensions.yml', 'r') as content:
      extensions = yaml.safe_load(content)

      if extension in extensions:
        files[file]['lookat'] = extensions[extension]
      else:
        files[file]['lookat'] = extension

  for file in files:
    lookat = files[file]['lookat']
    code = opacity_str('')
    config = {
      'colors': [],
      'regexes': []
    }

    with open(f'langs/{lookat}.yml', 'r') as content:
      gps = yaml.safe_load(content)

      for key in config.keys():
        if key in gps.keys():
          config[key] = gps[key]

    with open(file, 'r') as content:
      code.setStr(''.join(content.readlines()))

    for gp in config['regexes']:
      regexes = gp['regex']
      color = gp['color']
      important = False

      if type(regexes) != list:
        regexes = [regexes]

      if 'important' in gp.keys():
        important = bool(gp['important'])

      if color in config['colors']:
        color = config['colors'][color]
      else:
        if len(re.findall(r'[0-9\;]+', str(color))) == 0:
          color = 37

      for regex in regexes:
        values = arrRemDup(re.findall(regex, code.str))

        for val in values:
          pos = whereare(code.str, val)

          for x in pos:
            code.add(f'\033[{color}m', x)
            code.add(f'\033[0m', x + len(val))

            if important:
              code.remove(x, x + len(val))

    print(code.res)

if __name__ == '__main__':
  main()
