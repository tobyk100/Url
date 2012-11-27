class URL:
  def __init__(self, url):
    self.__url = url

  def isValid(self):
    regex = re.match(
      r'^(?:http|ftp)s?://'  # http:// or https://
      r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
      r'localhost|'  # localhost...
      r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
      r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
      r'(?::\d+)?'  # optional port
      r'(?:/?|[/?]\S+)$', self.__url, re.IGNORECASE)
    return validate_url(self.__url)

  def getNormalized(self):
    canonicalize_url(self.__url)

  def __len__(self):
    return len(self.normalized)

  def __getitem__(self, index):
    return self.normalized[index]

  # Comparison using normalized url
  def __lt__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() > other.isValid()
    else:
      return self.normalized < other.normalized

  def __le__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() > other.isValid()
    else:
      return self.normalized <= other.normalized

  def __gt__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() < other.isValid()
    else:
      return self.normalized > other.normalized

  def __ge__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() < other.isValid()
    else:
      return self.normalized >= other.normalized

  def __eq__(self, other):
    if self.isValid() != other.isValid():
      return False
    else:
      return self.normalized == other.normalized
