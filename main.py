#!/usr/bin/env python3

from sqlite3 import connect
import sys
import yaml
import re

def arrRemDup(arr):
  res = []

  for item in arr:
    if item not in res:
      res.append(item)

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
    config = {}

    with open(f'langs/{lookat}.yml', 'r') as content:
      config = yaml.safe_load(content)

    with open(file, 'r') as content:
      files[file]['code'] = ''.join(content.readlines())

      for gx in config['regexes']:
        regex = gx['regex']
        color = str(config['colors'][gx['color']])

        for item in arrRemDup(re.findall(regex, files[file]['code'])):
          files[file]['code'] = re.sub(
            item,
            f'\033[{color}m{item}\033[0m',
            files[file]['code']
          )

  for file in files:
    print(files[file]['code'])

if __name__ == '__main__':
  main()
