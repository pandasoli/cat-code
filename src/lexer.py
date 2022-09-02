import re
import enum


Alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numbers = '0123456789'

class TokenKind(enum.Enum):
  Identifier = 'Indentifier'
  Unknown = 'Unknown'

  String = 'String'
  Bracket = 'Bracket'
  Number = 'Number'
  MathChar = 'MathChar'
  Important = 'Important'
  KeyWord = 'KeyWord'
  Comment = 'Comment'
  Error = 'Error'
  Warning = 'Warning'


class Token:
  def __init__(self, kind, literal):
    self.kind = kind
    self.literal = literal


class Lexer:
  def __init__(self, contents, config):
    self.source = list(contents)
    self.config = config
    self.counter = 0

  def lex(self):
    tokens = []

    while len(self.source) > self.counter:
      if   self.search('comment'):    tokens.append(self.do('comment',    TokenKind.Comment   ))
      elif self.search('warning'):    tokens.append(self.do('warning',    TokenKind.Warning   ))
      elif self.search('error'):      tokens.append(self.do('error',      TokenKind.Error     ))
      elif self.search('bracket'):    tokens.append(self.do('bracket',    TokenKind.Bracket   ))
      elif self.search('math-char'):  tokens.append(self.do('math-char',  TokenKind.MathChar  ))
      elif self.search('keyword'):    tokens.append(self.do('keyword',    TokenKind.KeyWord   ))
      elif self.search('string'):     tokens.append(self.do('string',     TokenKind.String    ))
      elif self.search('number'):     tokens.append(self.do('number',     TokenKind.Number    ))
      elif self.search('important'):  tokens.append(self.do('important',  TokenKind.Important ))
      elif self.search('identifier'): tokens.append(self.do('identifier', TokenKind.Identifier))
      else:
        buffer = ''

        while True:
          if self.counter > len(self.source) - 1:
            break

          if self.search('comment') or self.search('warning') or self.search('error') or self.search('bracket') or self.search('math-char') or self.search('keyword') or self.search('string') or self.search('number') or self.search('important') or self.search('identifier'):
            break

          buffer += self.current_char()
          self.counter += 1

        tokens.append(Token(TokenKind.Unknown, buffer))

    return tokens

  def do(self, field, kind):
    buffer = self.getcurmatch(field)
    self.counter += len(buffer)
    return Token(kind, buffer)

  def getcurmatch(self, field):
    if field in self.config:
      return re.findall('^' + self.config[field], ''.join(self.source[self.counter:]))[0]
    return ''

  def search(self, field):
    if field in self.config:
      return len(
        re.findall('^' + self.config[field], ''.join(self.source[self.counter:]))
      ) > 0
    return False

  def current_char(self):
    return self.source[self.counter]
