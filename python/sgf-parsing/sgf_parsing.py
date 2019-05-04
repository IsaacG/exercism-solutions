import re

class SgfTree(object):
  def __init__(self, properties=None, children=None):
    self.properties = properties or {}
    self.children = children or []

  def __eq__(self, other):
    if not isinstance(other, SgfTree):
      return False
    for k, v in self.properties.items():
      if k not in other.properties:
        return False
      if other.properties[k] != v:
        return False
    for k in other.properties.keys():
      if k not in self.properties:
        return False
    if len(self.children) != len(other.children):
        return False
    for a, b in zip(self.children, other.children):
      if a != b:
        return False
    return True

  def __ne__(self, other):
    return not self == other


class Obj(object):
  def __init__(self, content):
    self.content = content
    self.Validate()

  def __repr__(self):
    return '%s(%s)' % (self.__class__.__name__, self.content)

  def ToSgf(self):
    raise NotImplemented

  def Validate(self):
    raise NotImplemented


class Properties(Obj):
  # If escaped input is not allowed:
  # PROPS_RE = re.compile(r'([A-Z]+)((?:\[\w+\])+)', re.DOTALL)
  # PROPVAL_RE = re.compile(r'\[\w+\]', re.DOTALL)

  PROPS_RE = re.compile(r'([A-Z]+)((?:\[.+?(?<!\\)\])+)', re.DOTALL)
  PROPVAL_RE = re.compile(r'\[.+?(?<!\\)\]', re.DOTALL)

  def Validate(self):
    if self.content and not self.PROPS_RE.match(self.content):
        raise ValueError('Badly formed properties.')

  def ToSgf(self):
    properties = {}
    for k, vals in self.PROPS_RE.findall(self.content):
      properties[k] = self.ParseAndCleanPropVals(vals)
    return properties

  def ParseAndCleanPropVals(self, vals):
    values = []
    for v in self.PROPVAL_RE.findall(vals):
      v = v[1:-1]  # Strip outer ()
      v = v.replace('\\', '')
      v = v.replace('\t', ' ')
      values.append(v)
    return values

class Node(Obj):
  def Validate(self):
    if not self.content.startswith(';'):
      raise ValueError('Malformed node')

  def Split(self):
    s = self.content[1:]
    if '(' in s and s.index('(') < s.index(';'):
      sep = '('
    else:
      sep = ';'
    p, s, c = s.partition(sep)
    return p, s+c

  def Properties(self):
    p, _ = self.Split()
    return Properties(p)

  def Children(self):
    _, c = self.Split()
    if c == '':
      return []
    elif c.startswith(';'):
      return [Node(c)]
    elif c.startswith('('):
      # Assuming no nesting.
      return [Node(n[1:-1]) for n in re.findall(r'\([^)]+\)', c)]
    else:
      raise ValueError('Badly formed children')

  def ToSgf(self):
    return SgfTree(
        self.Properties().ToSgf(),
        [node.ToSgf() for node in self.Children()])


class Tree(Obj):
  def Validate(self):
    s = self.content
    if not (s.startswith('(') and s.endswith(')')):
      raise ValueError('Malformed tree')

  def RootNode(self):
    return Node(self.content[1:-1])

  def ToSgf(self):
    return self.RootNode().ToSgf()
    


def parse(s):
  """Parse an SGF Tree."""
  return Tree(s).ToSgf()



# vim:ts=2:sw=2:expandtab
