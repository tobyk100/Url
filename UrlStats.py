from url_normalize import url_normalize
import sys
import re

"""
Parameters:
  urls - a list of urls to display stats for
Returns:
  A list of stat mappings, a stat mapping has the following fields:
    source: the source url
    canonicalzed: the canonicalized url
    valid: whether the url is valid
    source_unique: whether the source is unqiue amongst the urls list
    canonicalized_unique: like source_unique but for canonicalized urls
"""
def GetStats(urls):
  stats = {}
  canonicalized_list = [canonicalize_url(url) for url in urls]
  for url in urls:
    url_stat = {}
    canonicalized = canonicalize_url(url)
    url_stat['source'] = url
    url_stat['canonicalized'] = canonicalized
    url_stat['valid'] = validate_url(url)
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
def DisplayStats(url_stats):
  for stat in urls_stats:
    print "Source: {}\n".format(stat['source'])
    print "Valid: {}\n".format(stat['valid'])
    print "Canonical: {}\n".format(stat['canonicalized'])
    print "Source unique: {}\n".format(stat['source_unique'])
    print "Canonicalized URL unique: {}\n".format(stat['canonicalized_unique'])

def canonicalize_url(url):
  return url_normalize(url)

def validate_url(url):
  regex = re.match(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', url, re.IGNORECASE)

  return regex is not None

if __name__ == "__main__":
  if sys.argc != 2:
    print "Usage: " + argv[1] + " filename\n"
    sys.exit(1)

  try:
    file = open(filename, "rb")
  except IOError:
    print "Could not open " + filename + " for reading\n"
    sys.exit(1)

  urls = [line.strip() for line in file]
  stats = GetStats(urls)
  DisplayStats(stats)
  exit(0)
