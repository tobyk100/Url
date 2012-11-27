import re
from url_normalize import url_normalize
class Url:
  def __init__(self, url):
    self.url = url

  def isValid(self):
    regex = re.match(
      r'^(?:http|ftp)s?://'  # http:// or https://
      r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
      r'localhost|'  # localhost...
      r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
      r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
      r'(?::\d+)?'  # optional port
      r'(?:/?|[/?]\S+)$', self.url, re.IGNORECASE)

    return regex is not None

  def getNormalized(self):
    url_normalize(self.url)

  def __lt__(self, other):
    self.url < other.url

  def __le__(self, other):
    self.url <= other.url

  def __gt__(self, other):
    self.url > other.url

  def __ge__(self, other):
    self.url >= other.url

  def __eq__(self, other):
    self.url == other.url

  """
  Parameters:
    urls - a list of Url instance objects to display stats for
  Returns:
    A list of stat mappings, a stat mapping has the following fields:
      source: the source url
      canonicalzed: the canonicalized url
      valid: whether the url is valid
      source_unique: whether the source is unqiue amongst the urls list
      canonicalized_unique: like source_unique but for canonicalized urls
  """
  @staticmethod
  def GetStats(urls):
    stats = {}
    canonicalized_list = [url.getNormalized() for url in urls]
    for url in urls:
      url_stat = {}
      canonicalized = url.getNormalized()
      url_stat['source'] = url.url
      url_stat['canonicalized'] = canonicalized
      url_stat['valid'] = url.isValid()
      url_stat['source_unique'] = (urls.count(url) == 1)
      url_stat['canonicalized_unique'] = \
          (canonicalized_list.count(canonicalized) == 1)
      stats.add(url_stat)
    return stats

  """
  Parameters:
    url_stats - a list of url stats to display, see GetStats for more.
  Returns:
    Nothing
  Side Effects:
    Prints stats to stdout
  """
  @staticmethod
  def DisplayStats(url_stats):
    for stat in urls_stats:
      print "Source: {}\n".format(stat['source'])
      print "Valid: {}\n".format(stat['valid'])
      print "Canonical: {}\n".format(stat['canonicalized'])
      print "Source unique: {}\n".format(stat['source_unique'])
      print "Canonicalized URL unique: {}\n".format(stat['canonicalized_unique'])
