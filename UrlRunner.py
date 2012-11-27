import sys
from Url import Url

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

if __name__ == "__main__":
  if sys.argc != 2:
    print "Usage: " + argv[1] + " filename\n"
    sys.exit(1)

  try:
    file = open(filename, "rb")
  except IOError:
    print "Could not open " + filename + " for reading\n"
    sys.exit(1)

  urls = [Url(line.strip()) for line in file]
  stats = Url.GetStats(urls)
  DisplayStats(stats)
  exit(0)
